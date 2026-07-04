### Nom du défi
Compar:IA juridique

### Description courte
Compar:IA juridique est une arène de comparaison d'intelligences artificielles dédiée au droit français, réservée aux professionnels et futurs professionnels du droit, pour évaluer, grâce à leur expertise, quel modèle d'IA est réellement fiable sur des questions juridiques. Au-delà du classement, cette plateforme vise aussi à améliorer l'esprit critique des acteurs du droit face à l'IA générative, en les confrontant directement à ses limites, hallucinations, biais, et sources non vérifiées.

### Porteur
Simon Zilinskas

### Description longue
**Contexte :**

Compar:IA juridique est une plateforme qui reprend le principe d'une arène de comparaison d'IA conversationnelles appliquées spécifiquement au droit ; et elle donne aux professionnels du droit le pouvoir d'évaluer les intelligences artificielles selon leur fiabilité juridique.

Concrètement, en arrivant sur compar:IA juridique, le professionnel du droit pose une question juridique en langage naturel, et deux réponses apparaissent, générées par des modèles d'IA différents, sans qu'il sache lesquels. L'objectif est ensuite pour le professionnel du droit de sélectionner quelle réponse est la plus pertinente selon des critères préexistants ou en expliquant son choix en quelques lignes. Une fois son choix effectué, le professionnel découvre enfin quels modèles se cachaient derrière chaque réponse ; une révélation qui, au-delà du classement, l'entraîne à interroger systématiquement ce qu'une IA lui présente.

**Pourquoi ?**

La quasi-totalité des grands modèles d'IA sont entraînés sur des données très majoritairement anglo-saxonnes, pensées pour une logique de *common-law*, où le précédent et la jurisprudence l'emportent. Or la France, comme l'essentiel de l'Europe continentale, repose sur un droit romano-civiliste : c'est la loi écrite qui prime, pas le précédent. Notre classement révèle précisément quels modèles comprennent notre tradition juridique.

**Objectifs**

- Créer une arène sectorielle, adossée à compar:IA, réservée au domaine juridique.
- Réserver l'évaluation des réponses aux professionnels du droit, afin de garantir que l'évaluation réalisée fait autorité, et non de simples clics anonymes.
- Construire un classement des modèles d'IA fondé sur des critères juridiques précis et spécifiquement sur du droit français.
- Rendre ce classement public et accessible à tous.
- Rester maîtres de notre capacité à évaluer les IA dans une optique de souveraineté, pour mettre en avant celles qui comprennent réellement les spécificités du droit français.
- Constituer, à partir de ces évaluations, un jeu de données ouvert de préférences juridiques en français.

**Déroulé / fonctionnement**

1. **Arrivée sur la plateforme** : l'utilisateur pose une question juridique en langage naturel. Deux réponses apparaissent, produites par deux modèles d'IA différents, sans qu'il sache lesquels.
2. **Contrôle d'accès déclaratif** : à l'arrivée sur le site, il est demandé si l'utilisateur est un expert juridique ou un simple utilisateur. Nous fonctionnons sur la confiance déclarative, sans vérification bureaucratique lourde. Un expert entre dans l'arène ; un simple utilisateur est redirigé vers une page l'informant que l'accès est réservé.
3. **Évaluation par les experts** : face aux deux réponses, l'expert explique son choix en quelques lignes ou s'appuie sur des critères construits pour le droit :
   - **Pertinence juridique** : la réponse répond-elle à la question et est-elle conforme au droit en vigueur ?
   - **Actualisation** : les sources citées sont-elles à jour ?
   - **Transparence** : l'IA cite-t-elle ses sources ?
   - **Lisibilité** : la réponse est-elle claire ?
   - **Absence d'hallucination** : n'invente-t-elle ni réponse ni source ?
4. **Classement public** : les évaluations alimentent un classement mis à jour en continu, consultable par tous, experts comme grand public.

### Slogan
« Ne vous fiez pas aux réponses d'une seule IA (surtout dans le domaine juridique). »

### Image principale
![Image principale](https://docs.numerique.gouv.fr/media/4b6e8ac0-889c-4066-9a0a-2bce9cc51494/attachments/c09b421a-9da1-4b1a-8687-5cad0dbb8aa8.png)

### Contributeurs
- Simon Zilinskas (porteur)
- Dariia Haryfullina
- Pierre Montel
- Romane Mareschal
- Claire Demunck
- Ammâr Ouhmoudou
- Xavère Ricolfi

### Ressources utilisées
Cochez les ressources utilisées en remplaçant `[ ]` par `[x]`.

- [x] `openfisca-france-parameters` — Base de données de paramètres ✺ OpenFisca — utilisé indirectement (paramètres repris au sein des données agrégées par Moulineuse)
- [x] `an-dossiers-legislatifs` — Dossiers législatifs de l'Assemblée nationale (législature courante) ✺ Assemblée nationale — utilisé indirectement (ses données sont déjà présentes dans la base canutes de Moulineuse, accessible via droit_parlement)
- [x] `an-amendements-xvii` — Amendements déposés à l'Assemblée nationale (législature actuelle) ✺ Assemblée nationale — utilisé indirectement (couvert via Moulineuse)
- [x] `an-comptes-rendus` — Comptes rendus de la séance publique à l'Assemblée nationale (législature actuelle) ✺ Assemblée nationale — utilisé indirectement (couvert via Moulineuse)
- [x] `an-votes-xvii` — Votes des députés (législature actuelle) ✺ Assemblée nationale — utilisé indirectement (couvert via Moulineuse)
- [x] `an-deputes-en-exercice` — Députés en exercice ✺ Assemblée nationale — utilisé indirectement (couvert via Moulineuse)
- [x] `an-deputes-historique` — Historique des députés ✺ Assemblée nationale — utilisé indirectement (couvert via Moulineuse)
- [x] `an-deputes-senateurs-ministres-par-legislature` — Députés, sénateurs et ministres d'une législature ✺ Assemblée nationale — utilisé indirectement (couvert via Moulineuse)
- [x] `an-agenda-reunions` — Agenda des réunions à l'Assemblée nationale (législature courante) ✺ Assemblée nationale — utilisé indirectement (couvert via Moulineuse)
- [x] `an-questions-gouvernement` — Questions de l'Assemblée nationale au Gouvernement ✺ Assemblée nationale — utilisé indirectement (couvert via Moulineuse)
- [x] `an-questions-gouvernement-ecrites` — Questions écrites de l'Assemblée nationale au Gouvernement ✺ Assemblée nationale — utilisé indirectement (couvert via Moulineuse)
- [x] `an-questions-gouvernement-orales` — Questions orales de l'Assemblée nationale au Gouvernement ✺ Assemblée nationale — utilisé indirectement (couvert via Moulineuse)
- [x] `premier-ministre-legi` — Codes, lois et règlements consolidés ✺ Premier ministre — utilisé indirectement (couvert via le schéma legifrance de Moulineuse)
- [x] `premier-ministre-dole` — Dossiers législatifs Légifrance ✺ Premier ministre — utilisé indirectement (couvert via Moulineuse)
- [x] `premier-ministre-jorf` — Édition ''Lois et décrets'' du Journal officiel ✺ Premier ministre — utilisé indirectement (couvert via Moulineuse)
- [x] `senat-dispositifs-textes` — Dispositifs des textes déposés ou adoptés au Sénat ✺ Sénat — utilisé indirectement (couvert via le schéma sénat de Moulineuse)
- [x] `senat-dossiers-legislatifs` — Dossiers législatifs du Sénat ✺ Sénat — utilisé indirectement (couvert via Moulineuse)
- [x] `senat-amendements` — Amendements déposés au Sénat ✺ Sénat — utilisé indirectement (couvert via Moulineuse)
- [x] `senat-senateurs` — Sénateurs ✺ Sénat — utilisé indirectement (couvert via Moulineuse)
- [x] `senat-questions-gouvernement` — Questions orales et écrites du Sénat au Gouvernement ✺ Sénat — utilisé indirectement (couvert via Moulineuse)
- [x] `senat-comptes-rendus` — Comptes rendus de la séance publique au Sénat ✺ Sénat — utilisé indirectement (couvert via Moulineuse)
- [x] `an-et-co-database-regroupement-toutes-donnees` — Base de données unifiée Parlement / Législation / Service Public ✺ Assemblée nationale & communauté — utilisé indirectement (base Postgres derrière Moulineuse, consommée via le serveur MCP)
- [x] `an-et-co-serveur-mcp-regroupement-toutes-donnees` — Serveur MCP  - Accès unifié Parlement / Législation / Service Public ✺ Assemblée nationale & communauté — utilisé (il s'agit de Moulineuse, notre outil MCP droit_parlement)
- [x] `an-et-co-api-regroupement-toutes-donnees` — API - Accès unifié Parlement / Législation / Service Public ✺ Assemblée nationale & communauté — utilisé indirectement (mêmes données que Moulineuse, exposées ici en API REST)
- [x] `legiwatch-api-parlement` — API Parlement ✺ LegiWatch — utilisé indirectement (sous-ensemble parlementaire déjà couvert par Moulineuse)
- [x] `legiwatch-database-parlement` — Base de données Parlement ✺ LegiWatch — utilisé indirectement (idem)
- [x] `legiwatch-serveur-mcp-parlement` — Serveur MCP Parlement ✺ LegiWatch — utilisé indirectement (idem, Moulineuse en est un sur-ensemble strict)

### Galerie
_Aucune image pour le moment._

### Documents
- [Vidéo de démonstration](docs/demo.mp4)

### URL de démonstration
https://caddy-production-dab6.up.railway.app

### Diapositives de présentation
[Diapositives de présentation](docs/diapositives.pdf)
