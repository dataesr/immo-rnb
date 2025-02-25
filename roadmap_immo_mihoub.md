# Feuille de route : Analyse et Visualisation des Données sur la Vie Étudiante et l’Immobilier en France

## 1. Définition des Objectifs

Avant toute chose, clarifier les objectifs de l’analyse :

- **Répartition géographique des étudiants** : Où vivent-ils ? Quels sont les pôles universitaires les plus denses ?
- **Logement étudiant et accessibilité** :
  - Proximité des logements aux campus
  - Types de logements : CROUS, résidences privées, colocation, etc.
- **Qualité et durabilité des logements** :
  - État des infrastructures
  - Présence de logements écologiques
  - Présence de service de restauration aux étudiants
  - Service proposé par les infrastructures
  - Impact des politiques de rénovation
- **Impact des projets d’aménagement** : Quels sont les projets de construction ou de réhabilitation pour améliorer le logement étudiant ?
- **Corrélation avec les loyers** : Évolution des prix du logement étudiant par région.

---

## 2. Collecte des Données

### 📌 **Sources publiques et ouvertes**

- **Ministère de l'Enseignement Supérieur et de la Recherche** :  
  ➝ Données sur la répartition des étudiants, effectifs par académie.  
  [🔗 Accéder aux données](https://data.enseignementsup-recherche.gouv.fr)
  ➝ Ensemble des logements proposés aux étudiants par le réseau des CROUS
  [🔗 Jeu de donnée crous](https://data.enseignementsup-recherche.gouv.fr/explore/dataset/fr_crous_logement_france_entiere/information/)

- **INSEE** :  
  ➝ Données démographiques et immobilières sur les étudiants.  
  [🔗 Accéder aux statistiques](https://www.insee.fr/fr/statistiques)

- **Base DVF (Demande de Valeur Foncière)** :  
  ➝ Transactions immobilières, analyse des loyers.  
  [🔗 Accéder aux données](https://cadastre.data.gouv.fr/dvf)

- **Base des permis de construire (Sitadel)** :  
  ➝ Nouveaux logements et rénovations.  
  [🔗 Accéder aux datasets](https://www.data.gouv.fr/fr/datasets/sitadel/)

- **ADEME** :  
  ➝ Données sur les bâtiments écologiques et la rénovation énergétique.  
  [🔗 Accéder aux données](https://data.ademe.fr/)

- **CAF** :  
  ➝ Données sur les allocations des étudiants en fonction de leur status
  [🔗 Accéder aux données](https://explore.data.gouv.fr/fr/datasets/66d1e5ae79919854e97093cf/#/resources/a114fdca-2f73-4689-b840-9356cbcaee63)

### 📌 **Données complémentaires**

- **Plateformes immobilières** (_Seloger, Leboncoin, PAP, etc._) :
  - Scraping ou API pour récupérer des annonces de logements étudiants.
- **Données de transport** :
  - Accessibilité aux campus via les transports en commun (_via OpenStreetMap ou API locales_).
- **Témoignages et enquêtes étudiantes** :
  - Enquêtes locales ou via des syndicats étudiants (_UNEF, FAGE_).

---

## 3. Analyse des Données

### 🔍 **Exploration et prétraitement**

- **Nettoyage des données** :
  - Gestion des valeurs manquantes
  - Normalisation des données
- **Fusion des différentes bases** :
  - Croisement des données (_logements, étudiants, aménagements_)
- **Géocodage des adresses** pour la visualisation cartographique.

### 📊 **Analyses possibles**

- **Cartographie interactive** :

  - Répartition des étudiants par ville/région.
  - Localisation des logements étudiants et corrélation avec les loyers.
  - Présence des bâtiments écologiques.

- **Analyse des distances** :

  - Moyenne des distances **domicile-campus**.
  - Corrélation entre distance et coût du logement.

- **Étude des dynamiques de logement** :

  - Évolution des prix des logements étudiants par région.
  - Impact des rénovations sur le coût et la qualité de vie.

- **Prédiction et modèles** :
  - **Modélisation des flux étudiants** (_où se déplacent-ils ?_).
  - **Prédiction des besoins en logement** pour les prochaines années.