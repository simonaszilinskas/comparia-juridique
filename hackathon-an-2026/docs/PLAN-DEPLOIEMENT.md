# Plan de déploiement · compar:IA Juridique

**Stratégie d'acquisition d'évaluateurs qualifiés pour la constitution d'un jeu de données public sur la fiabilité des IA en droit français**

| | |
|---|---|
| **Projet** | compar:IA Juridique · déclinaison du comparateur compar:IA (beta.gouv.fr / DINUM) |
| **Cadre** | Hackathon de l'Assemblée nationale 2026 · challenge ComparIA Juridique |
| **Objectif** | 5 000 votes de juristes (plancher : 3 000) avant début novembre 2026 |
| **Moyens** | Budget : 0 € · équipe réduite · pilotage : Grist |
| **Version** | 1.0 · juillet 2026 |

---

## Sommaire

1. [Contexte et objectif](#1-contexte-et-objectif)
2. [Le raisonnement chiffré](#2-le-raisonnement-chiffré)
3. [Principes de déploiement](#3-principes-de-déploiement)
4. [Calendrier](#4-calendrier)
5. [Segments, canaux et séquences](#5-segments-canaux-et-séquences)
6. [Programme de relais](#6-programme-de-relais)
7. [Programme de webinaires d'acquisition](#7-programme-de-webinaires-dacquisition)
8. [Plan de tests](#8-plan-de-tests)
9. [Mesure et pilotage](#9-mesure-et-pilotage)
10. [Conformité et éthique](#10-conformité-et-éthique)
11. [Ressources du dépôt](#11-ressources-du-dépôt)
- [Annexe A · Les 15 messages prêts à l'emploi](#annexe-a--les-15-messages-prêts-à-lemploi)
- [Annexe B · Fiche d'exercice de TD](#annexe-b--fiche-dexercice-de-td)
- [Crédits](#crédits)

---

## 1. Contexte et objectif

Personne ne sait aujourd'hui quelle IA est réellement fiable en droit français. Les modèles juridiques spécialisés sont coûteux sans que leur supériorité soit démontrée ; les modèles généralistes sont largement utilisés par les juristes sans évaluation indépendante. compar:IA Juridique répond à ce vide : deux réponses d'IA anonymes à une question de droit, un vote, un jeu de données public.

La valeur du jeu de données dépend de la **qualité de l'évaluateur** : seul un juriste sait repérer un article inventé, un arrêt inexistant ou un syllogisme défaillant. La cible est donc exclusivement juridique : étudiants en droit (M1-M2), enseignants en droit, élèves-avocats (CRFPA, EFB), élèves ENM, étudiants d'IEP en masters droit, et praticiens (avocats, magistrats, juristes d'entreprise, juristes du secteur public, notaires, commissaires de justice). Population réellement atteignable estimée : **moins de 10 000 personnes**.

### Objectif calibré sur la significativité statistique

Le classement des modèles repose sur un système de type Elo / Bradley-Terry (méthodologie compar:IA). La robustesse du classement dépend du nombre de comparaisons (« batailles ») **par modèle**, avec une vingtaine de modèles en compétition et chaque vote faisant avancer deux modèles.

| Palier | Batailles / modèle | Ce que le jeu de données permet |
|---|---|---|
| **3 000 votes** (plancher) | ~300 | Classement global statistiquement significatif |
| **5 000 votes** (objectif) | ~500 | Classement solide + première lecture par grands domaines du droit |
| 30 000 votes (post-hackathon) | ~3 000 | Granularité par domaine · argument de pérennisation du service |

En résumé : **3 000 prouve, 5 000 classe, 30 000 cartographie.**

---

## 2. Le raisonnement chiffré

L'objectif est traduit en effort quotidien mesurable, à partir d'hypothèses de conversion prudentes recalibrées dès les premières données réelles.

```
5 000 votes  =  ~300 votes / semaine  =  ~45 votes / jour

5 000 votes
  ÷ 2 à 4 votes par session          →  ~1 700 à 2 500 utilisatrices et utilisateurs
  ÷ 25 à 35 % de taux de test        →  ~6 000 à 7 000 juristes touchés
```

6 000 à 7 000 personnes touchées sur une cible de moins de 10 000 : l'objectif exige de toucher la majorité de la cible atteignable. C'est impossible en contact individuel avec une équipe réduite. La stratégie repose donc sur les **multiplicateurs**, dont le rendement unitaire est sans commune mesure avec le contact direct :

| Levier | Rendement estimé |
|---|---|
| 1 enseignant qui fait tester en TD | 30 à 400 votes |
| 1 association étudiante qui relaie | 50 à 200 votes |
| 1 tribune dans un média juridique | milliers de lecteurs qualifiés |
| 1 message direct à un avocat | ~3 votes |

**Règle d'allocation : 80 % du temps sur les multiplicateurs, 20 % sur le contact direct** (qui sert principalement à tester les messages et à amorcer la preuve sociale).

À titre d'ordre de grandeur : une seule séance de travaux dirigés de 40 étudiants couvre plus de deux journées d'objectif.

---

## 3. Principes de déploiement

1. **Multiplicateurs d'abord.** Enseignants, associations étudiantes, administrateurs de groupes d'entraide, unions de jeunes avocats, incubateurs de barreaux.
2. **Le hook n'est pas le message institutionnel.** L'accroche universelle est la curiosité compétitive : *« Quelle IA est vraiment la meilleure en droit français ? Personne ne le sait. »* Les arguments souveraineté et gratuité arrivent en deuxième et troisième position.
3. **Un message par douleur, un canal par segment.** Le candidat CRFPA veut fiabiliser ses révisions ; le praticien veut savoir si un abonnement à 300 €/mois se justifie ; l'enseignant veut un exercice d'esprit critique clé en main.
4. **Jamais de spam.** Les étudiants ne sont jamais contactés directement : le passage se fait par les administrateurs de groupes et les associations, avec demande d'autorisation systématique.
5. **Tout est mesuré.** Pilotage hebdomadaire à partir de l'évolution du compteur de votes, mise en regard des actions menées et des pics observés ; la métrique de décision est le nombre de votes générés par heure de travail investie.

---

## 4. Calendrier

Le calendrier universitaire structure le plan : l'été est creux pour les facultés mais constitue le pic d'activité des candidats au CRFPA (examen en septembre), et la rentrée concentre l'essentiel du potentiel.

| Période | Réalité terrain | Actions |
|---|---|---|
| **Juillet** | Facultés vides · candidats CRFPA en révisions | Sprint CRFPA + praticiens · tests de messages · cartographie des multiplicateurs |
| **Août** | Creux général · pic de stress CRFPA | CRFPA en continu · kits de rentrée · fichier enseignants finalisé |
| **Septembre** | **La fenêtre décisive** : rentrée des facultés, EFB, IEJ · résultats d'admissibilité CRFPA | Activation simultanée : enseignants, associations, relais, exercices en TD |
| **Octobre** | Régime de croisière universitaire | Renforcement de ce qui fonctionne · classement inter-facultés · dernière ligne droite |

Estimation intermédiaire : les segments praticiens et CRFPA produisent 1 500 à 2 500 votes avant la rentrée ; septembre et octobre assurent le reste.

---

## 5. Segments, canaux et séquences

La cible est organisée en **trois segments opérationnels**, chacun associé à un canal unique et à une séquence de cinq messages (textes intégraux en [annexe A](#annexe-a--les-15-messages-prêts-à-lemploi)).

### Segment 1 · Praticiens

Avocats, magistrats, juristes d'entreprise, juristes du secteur public, notaires, commissaires de justice.

| | |
|---|---|
| **Canal** | LinkedIn (invitations avec note, 20/jour) + relais communautaires (UJA locales, incubateurs de barreaux, associations de juristes d'entreprise) |
| **Lancement** | Immédiat |
| **Douleur adressée** | « Dois-je payer un abonnement IA juridique à 200-400 €/mois, ou une IA généraliste gratuite suffit-elle ? » |
| **Séquence** | M1 note d'invitation → M2 présentation post-acceptation → M3 relance J+7 → M4 dernier message J+14 → M5 relais communautaire |

### Segment 2 · Enseignants

Professeurs et maîtres de conférences des facultés de droit, directeurs de M2, enseignants d'IEJ.

| | |
|---|---|
| **Canal** | Email professionnel public (pages universitaires), avec opt-out systématique |
| **Lancement** | Fin août (préparation des cours) |
| **Douleur adressée** | « Mes étudiants utilisent l'IA sans esprit critique et je n'ai pas de support neutre pour traiter le sujet » |
| **Levier** | 1 conversion = 1 promotion entière · exercice de TD clé en main fourni ([fiche pédagogique en annexe B](#annexe-b--fiche-dexercice-de-td), taxonomie de Bloom, 20 minutes, zéro préparation) |
| **Séquence** | M1 premier email → M2 relance J+5 avec l'exercice → M3 relance J+12 avec preuve sociale → M4 envoi de la fiche TD → M5 relance finale avec résultats intermédiaires (fin octobre) |

### Segment 3 · Étudiants et élèves

Étudiants M1-M2, candidats CRFPA, élèves-avocats (EFB et écoles d'avocats), élèves et candidats ENM, étudiants d'IEP en masters droit.

| | |
|---|---|
| **Canal** | Exclusivement via relais : administrateurs de groupes (Facebook, Discord, WhatsApp), associations et BDE. Jamais de contact direct. |
| **Lancement** | CRFPA : immédiat (révisions estivales) · reste du segment : rentrée de septembre |
| **Douleur adressée** | « Je révise avec une IA sans savoir si ses réponses sont fiables » |
| **Séquence** | M1 demande d'autorisation à l'administrateur → M2 post dans le groupe (décliné par sous-public) → M3 second post preuve sociale J+10 → M4 proposition de relais aux associations → M5 relance finale avec classement (mi-octobre) |

---

## 6. Programme de relais

Le moteur de volume de la rentrée : **25 à 40 relais étudiants** (1 à 2 par grande faculté de droit, EFB, IEP), recrutés fin août-septembre via les segments 2 et 3.

- **Demande** : un partage dans le groupe WhatsApp de promotion, une story, éventuellement trois affiches en bibliothèque universitaire. Rien de plus.
- **Dotation** : kit prêt à l'emploi (texte de post, visuel, affiche A5) et position de leur établissement au classement.
- **Incentive** : classement hebdomadaire inter-facultés des établissements contributeurs, publié chaque semaine, et mention des contributeurs dans le jeu de données publié.
- **Rendement attendu** : 2 000 à 4 000 votes, le plus gros bloc unitaire du plan.

En complément, un travail éditorial continu : deux publications LinkedIn par semaine (série « l'IA face au droit français »), participation aux conversations IA + droit, et une tribune proposée à un média juridique de référence en septembre.

---

## 7. Programme de webinaires d'acquisition

Le webinaire est le format qui cumule les deux objectifs du plan : **générer des votes en direct** (une démonstration collective de 15 minutes avec 100 participants produit 200 à 300 votes) et **recruter des multiplicateurs** (chaque enseignant ou responsable d'association convaincu en webinaire vaut des dizaines de votes ensuite). Chaque session enregistrée devient en outre un replay public, asset de conversion permanent.

### Dispositif commun

| | |
|---|---|
| **Diffusion** | webinaire.numerique.gouv.fr (BigBlueButton, solution souveraine de la DINUM, gratuite) · relais LinkedIn Live pour le segment praticiens |
| **Format** | 45 minutes : 10 min de contexte · 20 min de démonstration collective avec votes en direct · 10 min d'échange avec l'invité · 5 min d'appel à action |
| **Animation** | Simon Zilinskas-Inta (Chief Product Officer de compar:IA) et Pierre Montel, avec un invité par session |
| **Inscription** | Formulaire avec consentement explicite (RGPD) · les inscrits sont relançables (rappel, replay) |
| **Replay** | Publié systématiquement, avec le lien de vote en description |
| **Mesure** | Nombre d'inscrits et de participants · pic de votes observé sur le compteur pendant la démonstration collective |

### Les 5 webinaires

| # | Période | Cible | Titre de travail | Invité pressenti | Objectif dominant |
|---|---|---|---|---|---|
| W1 | Mi-juillet | Candidats CRFPA | « Réviser le CRFPA avec l'IA sans se faire piéger » | Enseignant d'IEJ ou lauréat CRFPA de l'année précédente | Votes en direct |
| W2 | Fin août | Praticiens | « IA juridiques à 300 €/mois contre IA gratuites : le match en direct » | Avocat utilisateur (via UJA ou incubateur de barreau) | Votes + relais UJA |
| W3 | Mi-septembre | Enseignants | « Un exercice d'esprit critique clé en main pour vos TD » | Enseignant ayant testé l'exercice (fiche en annexe B présentée en direct) | Multiplicateurs : 1 participant convaincu = 1 promotion |
| W4 | Début octobre | Étudiants M1-M2 et associations | « Quelle IA pour vos cas pratiques ? Testez-les toutes en même temps » + lancement du classement inter-facultés | Responsable d'une association référente | Votes + recrutement de relais |
| W5 | Fin octobre | Tous segments + presse juridique | « Quelle IA est la meilleure en droit français ? Premiers résultats » | Universitaire en droit du numérique ou journaliste juridique | Preuve sociale + dernière ligne droite |

W5 joue un rôle particulier : c'est le webinaire de restitution intermédiaire, où la méthodologie du classement (système Elo, ouverture des données, souveraineté de l'infrastructure) est expliquée au grand public juridique. Il est proposé en avant-première aux médias juridiques.

### Communication d'acquisition (identique pour chaque webinaire)

| Échéance | Action | Canaux |
|---|---|---|
| J-14 | Annonce + ouverture des inscriptions | Canal du segment visé (groupes via administrateurs, emails enseignants, UJA) + publication LinkedIn |
| J-7 | Relance avec l'angle de l'invité | Mêmes canaux + relais demandé à l'invité sur son propre réseau |
| J-1 | Rappel aux inscrits | Email direct (consentement recueilli à l'inscription) |
| Jour J | Démonstration collective = pic de votes observable sur le compteur | Lien projeté à l'écran |
| J+1 | Replay + lien de vote aux inscrits absents (taux de présence attendu : 35 à 45 %) | Email + publication LinkedIn + description du replay |

La promotion s'appuie exclusivement sur les canaux et relais déjà construits dans les sections 5 et 6 : aucun canal nouveau à créer, le webinaire est un contenu qui circule dans les tuyaux existants.

**Rendement attendu du programme : 800 à 2 000 votes directs** (live + replays), auxquels s'ajoutent les votes indirects des multiplicateurs recrutés en W3 et W4.

---

## 8. Plan de tests

Aucune hypothèse de message n'est considérée comme acquise. Les deux premières semaines sont consacrées à quatre tests, chacun mené sur une fenêtre dédiée pour rendre ses effets lisibles sur le compteur de votes.

| Test | Dispositif | Variantes | Métrique |
|---|---|---|---|
| 1 · Accroche | 90 messages praticiens (30 par variante) | Curiosité vs économique vs souveraineté | Taux de réponse + taux de clic |
| 2 · Format | Publications en groupes CRFPA (avec accord des administrateurs) | Post utilitaire vs post défi | Clics / taille du groupe |
| 3 · Longueur | 40 emails enseignants (fin août) | 5 lignes vs 10 lignes | Taux de réponse |
| 4 · Canal | Semaine 1 | Messages LinkedIn vs forums étudiants vs publication personnelle | **Votes générés par heure investie** |

**Décision en fin de semaine 2** : les deux combinaisons accroche × canal les plus rentables sont conservées, les autres sont abandonnées. La métrique d'arbitrage unique est le nombre de votes générés par heure de travail investie, seule métrique pertinente pour une équipe réduite.

---

## 9. Mesure et pilotage

### Instrumentation

- **Base de pilotage Grist**, trois tables :
  1. *Multiplicateurs* : identité, segment, canal, statut, actions réalisées
  2. *Séquences* : messages envoyés, dates, prochaines relances
  3. *Dashboard hebdomadaire* : évolution du compteur de votes, actions de la semaine mises en regard des pics observés, votes par heure investie, classement des établissements

### Rituel de pilotage

30 minutes chaque lundi : votes de la semaine comparés à l'objectif de 300, trois meilleures sources, une décision de réallocation (doubler ce qui fonctionne, arrêter ce qui ne fonctionne pas).

### Indicateurs de succès

| Indicateur | Cible |
|---|---|
| Votes cumulés début novembre | ≥ 5 000 (plancher : 3 000) |
| Batailles par modèle | ≥ 500 (plancher : 300) |
| Part de votes issus de multiplicateurs | ≥ 70 % |
| Diversité des questions | ≥ 1 000 questions distinctes |
| Relais actifs | ≥ 25 établissements |
| Webinaires | 5 sessions · ≥ 400 inscrits cumulés · ≥ 800 votes attribuables (live + replay) |

---

## 10. Conformité et éthique

Le plan s'inscrit dans les piliers du [manifeste beta.gouv.fr](https://beta.gouv.fr/manifeste) : primauté des besoins des utilisatrices et utilisateurs (un message par douleur réelle, jamais par besoin de la structure), pilotage par l'impact mesuré (section 9), amélioration continue par confrontation rapide au terrain (plan de tests, section 8) et transparence (le présent document est public). Il applique en outre les règles suivantes :

- **RGPD** : prospection B2B fondée sur l'intérêt légitime, exclusivement à partir d'adresses professionnelles publiques (pages universitaires, sites de cabinets) ; mention d'opt-out claire dans chaque email ; aucune collecte ni aucun scraping d'adresses étudiantes.
- **Consentement des espaces communautaires** : aucun message n'est publié dans un groupe sans l'accord préalable de ses administrateurs.
- **Transparence** : chaque message identifie le projet, son caractère public et gratuit, et l'usage des votes (jeu de données ouvert de recherche).
- **Données ouvertes** : les votes alimentent un jeu de données publié en open data, conformément à la démarche compar:IA.
- **Absence d'incentive matérielle** : la seule contrepartie proposée est la contribution à la recherche publique et la reconnaissance des contributeurs. Aucun tirage au sort, aucune récompense.

---

## 11. Ressources du dépôt

| Ressource | Emplacement | Usage |
|---|---|---|
| Fiche d'exercice de TD (1 page, taxonomie de Bloom) | [Annexe B ci-dessous](#annexe-b--fiche-dexercice-de-td) | Jointe aux emails enseignants (M2 et M4) · projetable en séance |
| Les 15 messages prêts à l'emploi | [Annexe A ci-dessous](#annexe-a--les-15-messages-prêts-à-lemploi) | Copier-coller par l'équipe, en remplaçant `[lien]`, `[Nom]` et les statistiques du moment |

---

## Annexe A · Les 15 messages prêts à l'emploi

Conventions : vouvoiement systématique · un seul lien par message · opt-out explicite sur tous les emails · `J+x` = jours après le message précédent en l'absence de réponse.

### Segment 1 · Praticiens (LinkedIn)

**M1 · Note d'invitation LinkedIn (300 caractères max)**

> Bonjour Maître, je participe à un projet public (issu de compar:IA, beta.gouv) qui évalue la fiabilité des IA sur le droit français. Personne ne sait aujourd'hui quelle IA est la meilleure en droit. Votre regard de praticien m'intéresse.

*Variante juriste d'entreprise : remplacer « Maître » par « Bonjour [Prénom] ».*

**M2 · Après acceptation (dans les 24 h)**

> Merci pour l'ajout !
>
> Le projet en deux phrases : compar:IA Juridique vous donne deux réponses d'IA anonymes à n'importe quelle question de droit. Vous comparez, vous votez pour la meilleure, et vous découvrez ensuite quels modèles ont répondu. Vos votes alimentent une évaluation publique et indépendante des IA sur le droit français.
>
> Concrètement pour vous : avant de payer un abonnement IA juridique à 200 ou 400 € par mois, vous pouvez vérifier vous-même si les modèles spécialisés font réellement mieux que les généralistes gratuits.
>
> C'est gratuit, sans création de compte, et une question de votre pratique quotidienne suffit pour tester : [lien]

**M3 · Relance J+7**

> Bonjour [Prénom],
>
> Avez-vous eu l'occasion de tester ? Le retour qui revient le plus chez les confrères qui l'ont fait : la surprise. Les modèles les plus chers ne sont pas systématiquement les plus fiables sur le droit français.
>
> Si vous testez sur une vraie question de votre pratique, je suis preneur de votre verdict, c'est exactement le type de retour qui fait la valeur du projet : [lien]

**M4 · Dernier message individuel J+14**

> Bonjour [Prénom],
>
> Dernier message, promis. La collecte des votes se termine début novembre.
>
> Un vote de praticien pèse plus lourd que dix votes de non-juristes : vous savez repérer une réponse fausse, une jurisprudence inventée, un article de code mal cité. C'est cette expertise qui rend le jeu de données utile.
>
> 3 minutes, une question, deux réponses, un vote : [lien]
>
> Dans tous les cas, merci pour votre temps et bonne continuation.

**M5 · Relais communautaires (présidents d'UJA, responsables d'incubateurs de barreaux, associations de juristes d'entreprise)**

> Bonjour [Prénom],
>
> Je me permets de vous écrire en tant que [président de l'UJA de X / responsable de l'incubateur du barreau de X].
>
> Nous menons un projet public d'évaluation des IA sur le droit français : compar:IA Juridique (issu du comparateur compar:IA de beta.gouv). Le principe : deux réponses d'IA anonymes à une question de droit, l'utilisateur vote pour la meilleure, les votes construisent un classement public et indépendant.
>
> Vos membres sont exactement le public dont ce projet a besoin : des juristes en exercice, capables de juger la qualité d'une réponse juridique.
>
> Seriez-vous ouvert à un simple partage du lien dans votre newsletter ou votre groupe ? Je peux aussi faire une démonstration de 10 minutes lors d'un de vos événements si c'est plus simple. Aucun enjeu commercial, le projet est public et gratuit.
>
> Le lien : [lien]

### Segment 2 · Enseignants (email professionnel public)

**M1 · Premier email**
**Objet : Vos étudiants utilisent déjà l'IA · autant que ça serve à quelque chose**

> Bonjour Professeur [Nom],
>
> Vos étudiants utilisent ChatGPT pour préparer leurs TD, vous le savez. Ce que personne ne sait en revanche, c'est quelle IA est réellement fiable en droit français.
>
> compar:IA Juridique (issu de compar:IA, beta.gouv) permet de comparer deux IA en aveugle sur une question juridique et de voter pour la meilleure réponse. Chaque vote alimente un jeu de données public de recherche sur la fiabilité des IA en droit.
>
> C'est gratuit, sans compte, et cela fait un excellent exercice de TD : esprit critique, méthodologie juridique et compréhension de l'IA en une seule séance.
>
> 15 minutes suffisent pour voir si cela peut vous servir : [lien]
>
> Bien cordialement,
> [Prénom Nom]
>
> Si vous ne souhaitez plus recevoir de message de ma part, dites-le moi simplement.

**M2 · Relance J+5 (même fil)**
**Objet : RE: Vos étudiants utilisent déjà l'IA**

> Bonjour Professeur [Nom],
>
> Une précision qui peut vous être utile : l'exercice type prend 20 minutes en TD.
>
> L'étudiant pose une vraie question de droit (celle du cas pratique de la semaine, par exemple), reçoit deux réponses anonymes, vote pour la meilleure, puis découvre quels modèles il vient d'évaluer. Le débriefing porte sur ce qui distingue une bonne réponse juridique : sources exactes, raisonnement, absence d'hallucination.
>
> Je peux vous envoyer une fiche d'exercice prête à l'emploi (1 page) si cela vous intéresse.
>
> Bien cordialement,
> [Prénom Nom]

**M3 · Relance J+12 (dernier message de la séquence courte)**
**Objet : RE: Vos étudiants utilisent déjà l'IA**

> Bonjour Professeur [Nom],
>
> Dernier message : plusieurs enseignants utilisent déjà l'outil en TD ce semestre, et les premiers résultats sur la fiabilité des modèles en droit français sont contre-intuitifs. Les modèles juridiques spécialisés et payants ne dominent pas systématiquement les modèles généralistes.
>
> Si le sujet vous intéresse pour vos enseignements ou vos recherches : [lien]
>
> Sinon, je ne vous relancerai plus. Merci pour votre attention.
>
> Bien cordialement,
> [Prénom Nom]

**M4 · Envoi de la fiche TD (aux répondants et cliqueurs)**
**Objet : Fiche d'exercice TD · compar:IA Juridique**

> Bonjour Professeur [Nom],
>
> Comme promis, voici la fiche d'exercice (1 page, en pièce jointe) : objectifs pédagogiques structurés selon la taxonomie de Bloom, déroulé en 20 minutes, grille d'analyse, questions de débriefing. Elle est libre de réutilisation et d'adaptation.
>
> Le lien à projeter en séance : [lien]
>
> Si vous l'utilisez, un simple retour de votre part (ce qui a marché, ce qui a surpris les étudiants) m'intéresse beaucoup.
>
> Bien cordialement,
> [Prénom Nom]

**M5 · Relance finale à toute la base (fin octobre)**
**Objet : IA et droit français : les premiers résultats (et les 3 dernières semaines pour contribuer)**

> Bonjour Professeur [Nom],
>
> Un point d'étape avant la clôture de la collecte début novembre : [X] votes de juristes ont été recueillis, et les premiers enseignements sont là. [Insérer une statistique frappante.]
>
> Si vous souhaitez que vos étudiants contribuent au jeu de données final, c'est le moment : une séance de TD ou un simple partage du lien suffit.
>
> [lien]
>
> Merci à tous ceux qui ont déjà participé. Les résultats complets seront publics.
>
> Bien cordialement,
> [Prénom Nom]

### Segment 3 · Étudiants et élèves (via relais uniquement)

**M1 · Demande d'autorisation à l'administrateur du groupe ou de l'association**

> Bonjour,
>
> Je fais partie de l'équipe qui travaille sur compar:IA Juridique, la déclinaison droit du comparateur d'IA de beta.gouv. C'est un outil public et gratuit : on pose une question de droit, on reçoit deux réponses d'IA anonymes, on vote pour la meilleure, et on découvre quels modèles ont répondu.
>
> C'est très utile en période de révisions pour croiser les sources au lieu de faire confiance à une seule IA, et chaque vote alimente un jeu de données public de recherche.
>
> Est-ce que je peux le partager dans le groupe, ou préférez-vous le poster vous-même ? Aucun objectif commercial, c'est un projet d'intérêt général. Je peux vous envoyer un texte prêt à publier si c'est plus simple.

**M2 · Post dans le groupe (une fois l'accord obtenu) · version CRFPA**

> Pour ceux qui utilisent l'IA dans leurs révisions : arrêtez de faire confiance à une seule IA.
>
> compar:IA Juridique (beta.gouv) vous donne deux réponses anonymes à chaque question de droit. Vous comparez, vous votez, vous découvrez quels modèles ont répondu. Parfait pour vérifier une notion de cours ou un point de procédure en croisant deux sources d'un coup.
>
> Gratuit, sans compte, et chaque vote fait avancer la recherche publique sur la fiabilité des IA en droit français.
>
> [lien]

*Version M1-M2 : première ligne remplacée par « Pour vos fiches, vos cas pratiques et vos mémoires : arrêtez de faire confiance à une seule IA. » · Version ENM : « Entraînez votre esprit critique : repérez ce qu'une IA rate qu'un magistrat ne raterait pas. »*

**M3 · Second post J+10 (preuve sociale)**

> Petit retour après [X] votes de juristes sur compar:IA Juridique : le modèle le mieux classé sur les questions de droit français n'est pas celui qu'on croit. [Adapter avec la statistique du moment.]
>
> Testez sur vos propres questions de révision et voyez si vous êtes d'accord avec le classement : [lien]

**M4 · Proposition de relais aux associations et BDE (rentrée)**

> Bonjour,
>
> On cherche une association par établissement pour faire connaître compar:IA Juridique à la rentrée : un post, une story, et si vous êtes motivés une affiche en BU. Zéro budget, zéro pub, c'est un projet public de recherche sur la fiabilité des IA en droit.
>
> Ce qu'on vous donne : un texte prêt à publier et un visuel. On publie chaque semaine le classement des établissements qui contribuent le plus au jeu de données : autant que [nom de l'établissement] soit dans le haut du tableau.
>
> Partant ? Je vous envoie le kit dans la journée.

**M5 · Relance finale aux relais actifs (mi-octobre)**

> Bonjour,
>
> Dernière ligne droite : la collecte se termine début novembre et il manque [X] votes pour atteindre l'objectif.
>
> Classement actuel des établissements contributeurs : 1. [établissement] · 2. [établissement] · 3. [établissement].
>
> Un dernier post de votre part cette semaine peut faire la différence, aussi bien pour le classement que pour la qualité du jeu de données final (qui sera public, avec les contributeurs remerciés).
>
> Le lien : [lien]
>
> Merci pour tout ce que vous avez déjà relayé.

---

## Annexe B · Fiche d'exercice de TD

# Exercice de TD · Évaluer la fiabilité des IA en droit français

*avec compar:IA Juridique · comparateur d'IA en aveugle · issu de compar:IA (beta.gouv.fr)*

| Public | Durée | Matériel | Préparation |
|---|---|---|---|
| L3 à M2 · IEJ | 20 minutes | Smartphone ou ordinateur | Aucune · sans compte |

### Objectifs pédagogiques · taxonomie de Bloom (révisée)

| Niveau | Objectif |
|---|---|
| **Comprendre** | Expliquer le fonctionnement probabiliste d'une IA générative et pourquoi elle peut produire des hallucinations juridiques. |
| **Appliquer** | Mettre en œuvre la grille d'analyse ci-dessous sur une réponse d'IA à une question de droit réelle. |
| **Analyser** | Décomposer une réponse juridique en ses éléments (sources, qualification, syllogisme) et repérer erreurs et hallucinations. |
| **Évaluer** | Comparer deux argumentaires, porter un jugement motivé (le vote) et justifier ses critères devant le groupe. |
| **Créer** | Prolongement : rédiger la réponse corrigée et sourcée que l'IA aurait dû produire (voir variantes). |

### Déroulé minuté

| Temps | Étape |
|---|---|
| **0-3 min** | **Lancement.** Projeter le lien ou le QR code. Chaque étudiant ouvre compar:IA Juridique. Consigne : « Vous allez poser une vraie question de droit à deux IA anonymes, puis voter pour la meilleure réponse. » |
| **3-10 min** | **Comparaison individuelle.** Chaque étudiant pose la question du cas pratique de la semaine (ou une question de son choix : notion de cours, point de procédure, question de révision). Il lit les deux réponses avec la grille d'analyse ci-dessous. |
| **10-15 min** | **Vote et révélation.** Chaque étudiant vote pour la meilleure réponse (ou égalité), puis découvre quels modèles ont répondu. Encourager 2 à 3 questions-votes par étudiant si le temps le permet. |
| **15-20 min** | **Débriefing collectif.** Tour de table à partir des questions ci-dessous. Conclure sur la règle d'or : une réponse d'IA est un point de départ à vérifier, jamais une source citable. |

### Grille d'analyse d'une réponse juridique produite par une IA

| Critère | Questions à se poser |
|---|---|
| **Sources** | Les textes cités existent-ils ? Les numéros d'articles sont-ils exacts ? La jurisprudence mentionnée est-elle réelle et bien référencée ? |
| **Raisonnement** | Le syllogisme juridique est-il correct ? La qualification des faits est-elle pertinente ? Les conditions d'application de la règle sont-elles toutes examinées ? |
| **Actualité** | L'état du droit présenté est-il à jour ? Une réforme récente ou un revirement de jurisprudence est-il ignoré ? |
| **Prudence** | La réponse signale-t-elle ses incertitudes et ses limites, ou affirme-t-elle avec un aplomb injustifié ? |

### Questions de débriefing (alignées sur les niveaux visés)

1. **[Analyser]** Qu'est-ce qui a fait la différence entre les deux réponses ? Auriez-vous voté pareil avant la révélation des modèles ?
2. **[Analyser]** Quelqu'un a-t-il repéré une hallucination (article inventé, arrêt inexistant, règle déformée) ? Comment l'a-t-il détectée ?
3. **[Évaluer]** Le modèle que vous utilisez habituellement a-t-il gagné ? Sur quels critères fondez-vous votre jugement ?
4. **[Évaluer]** Dans quels cas un juriste peut-il s'appuyer sur une IA, et dans quels cas est-ce une faute professionnelle en devenir ?

### Variantes

- **Cas pratique** : tous les étudiants posent la même question issue du cas de la semaine, puis comparent les classements.
- **Préparation CRFPA / concours** : questions de méthodologie et de procédure, chasse aux hallucinations chronométrée.
- **Niveau Créer (+20 min ou travail maison)** : chaque étudiant rédige la réponse corrigée et sourcée que l'IA aurait dû produire, avec références vérifiées.

> **Pourquoi cet exercice compte au-delà du TD** : chaque vote alimente un jeu de données public de recherche sur la fiabilité des IA en droit français (méthodologie compar:IA, beta.gouv.fr). Une séance de TD de 40 étudiants produit environ 100 évaluations qualifiées. Les résultats seront publiés en données ouvertes.

---

## Crédits

**Projet porté par [Simon Zilinskas-Inta](https://www.linkedin.com/in/simonaszilinskas/), entrepreneur d'intérêt général de compar:IA.**

Équipe du hackathon :

- [Pierre Montel](https://www.linkedin.com/in/pierremontel/)
- [Xavère Ricolfi](https://www.linkedin.com/in/xavere/)
- [Claire de Munck](https://www.linkedin.com/in/clairedemunck/)
- [Romane Mareschal](https://www.linkedin.com/in/romane-mareschal-3bb206256/)
- [Dariia Haryfullina](https://www.linkedin.com/in/darhrf/)

---

*Équipe compar:IA Juridique · Hackathon de l'Assemblée nationale 2026 · Document publié en juillet 2026 sous [Licence Ouverte 2.0 (Etalab)](https://www.etalab.gouv.fr/licence-ouverte-open-licence/).*
