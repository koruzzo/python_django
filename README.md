# Python_Django

## Introduction

Ce projet vise à construire un entrepôt de données (data warehouse) à l'aide du framework Django. L'objectif est d'importer des données provenant de différentes sources dans des tables de faits (fact tables) et de dimensions (dimension tables), puis d'effectuer des analyses sur ces données.

Le projet est organisé de la manière suivante :

- **scripts**: Contient les scripts Python utilisés pour l'extraction, la transformation et le chargement des données.
- **api**: Répertoire Django où sont définis les modèles de données DWH et l'API pour accéder à ces données.
- **app**: Répertoire Django où sont définis les modèles de données ODS.

## Dépendances et Configuration

Avant de lancer l'application, assurez-vous d'avoir toutes les dépendances installées affichées dans le fichier `requirements.txt`.

Vous pouvez installer les dépendances en exécutant :
`pip install -r requirements.txt`


## Installation

1. Cloner ce dépôt sur votre machine locale.
2. Assurez-vous d'avoir Python et Django installés sur votre machine.
3. Configurez votre base de données dans `settings.py`.
4. Exécutez les migrations Django pour créer les tables de base de données nécessaires.
5. Les CSV n'ont pas été exportés sur GitHub, il vous faut les dedmander.
6. Exécutez `ELT_ODS.py` et `ELT_ODS2.py` avec `python manage.py runscript nom_du_script`.
7. Exécutez ensuite les scripts `DWH_SAT.py`, `DWH_DATE.py`,`DWH_LOCALISATION.py`,`DWH_FEDERATION.py`,`DWH_CLUB.py` et `DWH_LICENCE` avec `python manage.py runscript nom_du_script`.

## Usage

Une fois Docker lancé et configuré, vous pouvez accéder à l'API via le lien local et les URLs définies.

*"http://localhost:8000/api/end-point-dwh/?table=NOM_DE_LA_CLASSE"*
ou
*"http://localhost:8000/admin"*
puis cliquez sur les liens sous "API Links" pour accéder aux données de l'entrepôt de données.