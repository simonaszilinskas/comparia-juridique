import asyncio
import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from prometheus_fastapi_instrumentator import Instrumentator

from backend.admin.router import router as admin_router
from backend.arena.router import router as arena_router
from backend.auth.middleware import auth_middleware
from backend.auth.router import router as auth_router
from backend.config import RANKING_RECOMPUTE_INTERVAL_SECONDS, settings
from backend.llms.router import router as models_router
from backend.logger import configure_logger, configure_uvicorn_logging
from backend.sentry import init_sentry
from backend.utils.countries import get_vote_count

logger = logging.getLogger("languia")


async def _periodic_ranking_recompute():
    """Recompute the ranking on a timer, independent of vote traffic, so the
    Redis cache's 24h TTL never lapses on a quiet instance."""
    from utils.ranking.run import main as compute_and_store_ranking

    while True:
        try:
            await compute_and_store_ranking(mode="redis")
        except Exception:
            logger.exception("[RANKING] Periodic recompute failed")
        await asyncio.sleep(RANKING_RECOMPUTE_INTERVAL_SECONDS)


@asynccontextmanager
async def lifespan(app: FastAPI):
    if settings.COMPARIA_DB_URI and settings.ADMIN_EMAILS:
        from utils.database.actions.seed import seed_admins

        await seed_admins()

    task = asyncio.create_task(_periodic_ranking_recompute())
    try:
        yield
    finally:
        task.cancel()


app = FastAPI(lifespan=lifespan)

logger = configure_logger()
configure_uvicorn_logging()
# Log séparateur au démarrage pour marquer les redémarrages
logger.info("=" * 80)

init_sentry()


origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://localhost:3001",
    "http://localhost:3002",
    "http://localhost:5173",
    "http://localhost:5174",
    "http://localhost:8000",
    "http://localhost:8001",
    "http://localhost:8002",
    "http://localhost:8008",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.middleware("http")(auth_middleware)

# Prometheus metrics instrumentation
Instrumentator().instrument(app).expose(app, endpoint="/metrics")

app.include_router(models_router)
app.include_router(arena_router)
app.include_router(auth_router)
app.include_router(admin_router)


@app.get("/counter")
async def get_counter():
    return {
        "count": await get_vote_count(),
        "objective": settings.VOTES_OBJECTIVE,
    }
