from pydantic import BaseModel


class Skill(BaseModel):
    id: str
    label: str
    description: str
    prompt_content: str


AVAILABLE_SKILLS: dict[str, Skill] = {
    "privacy_policy_analysis": Skill(
        id="privacy_policy_analysis",
        label="Analyse de politique de confidentialité",
        description=(
            "Structure la réponse comme une analyse RGPD : finalités du traitement, "
            "base légale, données collectées, durées de conservation, transferts hors "
            "UE, droits des personnes concernées, et points de vigilance."
        ),
        prompt_content=(
            "Quand l'utilisateur te soumet ou te questionne sur une politique de "
            "confidentialité ou un traitement de données personnelles, structure ta "
            "réponse en sections claires : (1) finalités du traitement, (2) base "
            "légale invoquée (art. 6 RGPD), (3) données collectées et durées de "
            "conservation, (4) transferts hors Union européenne le cas échéant, "
            "(5) droits des personnes concernées (accès, rectification, effacement, "
            "opposition), (6) points de vigilance ou clauses ambiguës/à risque. "
            "Cite les articles du RGPD pertinents. Précise que ton analyse est une "
            "aide à la lecture et ne remplace pas un avis juridique."
        ),
    ),
    "legal_reasoning": Skill(
        id="legal_reasoning",
        label="Raisonnement juridique (syllogisme)",
        description=(
            "Structure l'analyse d'un cas comme un magistrat français : faits, "
            "qualification juridique, règle de droit applicable (majeure), "
            "application aux faits (mineure), conclusion, et moyens des parties."
        ),
        prompt_content=(
            "Quand l'utilisateur soumet un cas, un litige ou une question de droit "
            "à analyser, structure ta réponse selon le syllogisme judiciaire "
            "utilisé par les juridictions françaises : (1) rappel synthétique des "
            "faits pertinents, (2) qualification juridique des faits, (3) la règle "
            "de droit applicable (texte de loi, jurisprudence constante — la "
            "majeure), (4) l'application de cette règle aux faits de l'espèce (la "
            "mineure), (5) la conclusion qui en découle. Si le cas est contentieux, "
            "présente également les moyens qu'invoquerait chaque partie et évalue "
            "leurs chances de succès. Précise le degré d'incertitude quand la "
            "jurisprudence est divisée ou évolutive, et que cette analyse ne "
            "remplace pas la consultation d'un avocat."
        ),
    ),
    "legal_citation_check": Skill(
        id="legal_citation_check",
        label="Vérification des références juridiques",
        description=(
            "Discipline anti-hallucination : n'invente jamais un article de loi, "
            "un arrêt ou une référence Légifrance, signale explicitement toute "
            "référence non vérifiée et recommande une vérification si les outils "
            "juridiques ne sont pas disponibles ou ne confirment pas la source."
        ),
        prompt_content=(
            "Chaque fois que tu cites un article de loi, un code, une décision de "
            "justice ou une référence Légifrance/Judilibre/EUR-Lex, tu dois soit "
            "l'avoir vérifiée via un outil disponible dans cette conversation, soit "
            "signaler explicitement qu'elle provient de ta mémoire et n'a pas été "
            "vérifiée dans cette session. N'invente jamais un numéro d'article, un "
            "numéro de pourvoi, une date ou un intitulé de décision : si tu n'es pas "
            "certain qu'une référence existe réellement, dis-le clairement plutôt "
            "que de la présenter comme certaine. Quand un outil de recherche "
            "juridique est disponible, utilise-le pour confirmer toute référence "
            "avant de l'inclure dans ta réponse finale. Rappelle en fin de réponse "
            "que les références non vérifiées doivent être recontrôlées sur "
            "Légifrance ou Judilibre avant tout usage professionnel."
        ),
    ),
    "procedural_document_drafting": Skill(
        id="procedural_document_drafting",
        label="Rédaction d'actes de procédure civile",
        description=(
            "Structure la rédaction d'une assignation, requête ou conclusions "
            "selon les mentions obligatoires du Code de procédure civile : "
            "juridiction saisie, exposé des faits, moyens, pièces, dispositif."
        ),
        prompt_content=(
            "Quand l'utilisateur demande de rédiger un acte de procédure civile "
            "(assignation, requête, conclusions), structure le document avec les "
            "mentions attendues par le Code de procédure civile : (1) juridiction "
            "saisie et sa compétence, (2) identification des parties, (3) exposé "
            "des faits, (4) discussion juridique et moyens invoqués (texte de loi "
            "et jurisprudence à l'appui), (5) bordereau de pièces communiquées, "
            "(6) dispositif récapitulant précisément ce qui est demandé au juge. "
            "Adapte le formalisme à la juridiction mentionnée par l'utilisateur "
            "(tribunal judiciaire, tribunal de commerce, conseil de prud'hommes) "
            "si elle est précisée. Signale les délais de procédure applicables "
            "quand ils sont pertinents (ex. délai de comparution en référé) et "
            "précise que le document doit être relu par un avocat avant tout dépôt."
        ),
    ),
    "termination_notice_drafting": Skill(
        id="termination_notice_drafting",
        label="Rédaction d'une notification de licenciement",
        description=(
            "Structure une lettre de licenciement conforme au droit du travail "
            "français : motif précis et matériellement vérifiable, respect de la "
            "procédure préalable, mentions obligatoires, préavis et indemnités."
        ),
        prompt_content=(
            "Quand l'utilisateur demande de rédiger ou de vérifier une lettre de "
            "notification de licenciement, structure la réponse en vérifiant : "
            "(1) que le motif énoncé est précis, objectif et matériellement "
            "vérifiable (une lettre insuffisamment motivée peut être requalifiée en "
            "licenciement sans cause réelle et sérieuse), (2) que la procédure "
            "préalable a bien été respectée (convocation à entretien préalable, "
            "délais légaux, assistance du salarié), (3) les mentions obligatoires "
            "selon le motif (disciplinaire, économique, inaptitude), (4) le "
            "préavis applicable et les indemnités dues (indemnité légale ou "
            "conventionnelle de licenciement, congés payés), (5) les voies et "
            "délais de contestation à rappeler au salarié le cas échéant. Cite les "
            "articles du Code du travail pertinents (notamment L1232 et suivants) "
            "et précise que le document doit être validé par un professionnel "
            "avant envoi, une erreur de motif ou de procédure exposant l'employeur "
            "à un risque contentieux devant le conseil de prud'hommes."
        ),
    ),
    "vendor_dpa_review": Skill(
        id="vendor_dpa_review",
        label="Revue d'un accord de sous-traitance (DPA)",
        description=(
            "Structure la revue d'un contrat de sous-traitance de données "
            "personnelles (DPA) au regard de l'article 28 du RGPD : mentions "
            "obligatoires, garanties du sous-traitant, clauses à risque."
        ),
        prompt_content=(
            "Quand l'utilisateur soumet un accord de sous-traitance de données "
            "personnelles (DPA/Data Processing Agreement) à analyser, vérifie sa "
            "conformité à l'article 28 du RGPD en structurant ta réponse ainsi : "
            "(1) objet, nature, finalité, durée et catégories de données/personnes "
            "concernées par le traitement sous-traité, (2) présence des "
            "obligations imposées au sous-traitant par l'art. 28§3 (agir sur "
            "instruction documentée, confidentialité, mesures de sécurité "
            "art. 32, recours à des sous-traitants ultérieurs, assistance au "
            "responsable de traitement, sort des données en fin de contrat, mise à "
            "disposition des informations nécessaires à l'audit), (3) présence et "
            "encadrement des transferts hors UE (clauses contractuelles types, "
            "décision d'adéquation), (4) clauses ambiguës, manquantes ou à risque "
            "pour le responsable de traitement. Précise que cette analyse est une "
            "aide à la relecture et ne remplace pas un avis juridique."
        ),
    ),
}
