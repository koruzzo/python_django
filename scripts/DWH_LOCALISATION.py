import sqlite3
import pandas as pd
from api.models import D_Localisation

def run():
    """Importe les données des tables app_club et app_club_2 dans le modèle D_Localisation."""
    conn = sqlite3.connect('db.sqlite3')

    # Charger les données de la table app_club avec la condition sur la région
    df_app_club = pd.read_sql_query("SELECT * FROM app_club WHERE region = 'Auvergne-Rhône-Alpes' AND code_commune != 'NR - Non réparti'", conn)

    # Charger les données de la table app_club_2 avec la condition sur la région
    df_app_club_2 = pd.read_sql_query("SELECT * FROM app_club_2 WHERE region = 'Auvergne-Rhône-Alpes' AND code_commune != 'NR - Non réparti'", conn)

    df_app_club_2 = df_app_club_2.loc[:, ~df_app_club_2.columns.str.contains('f_nr|h_nr|nr_nr')]

    # Créer une liste pour stocker les objets D_Localisation à créer
    localisations_to_create = []
    local_ids_created = set()

    # Parcourir les lignes de la table app_club
    for _, row in df_app_club.iterrows():
        code_commune = row['code_commune']
        code_qpv = row['code_qpv']
        local_id = code_commune + '-' + code_qpv

        # Vérifier si cette localisation n'a pas déjà été créée
        if local_id not in local_ids_created:
            # Créer un objet D_Localisation avec les données de la ligne actuelle
            localisation = D_Localisation(
                local_id=local_id,
                code_comu=code_commune,
                code_qpv=code_qpv,
                region=row['region'],
                departement=row['departement'],
                statut_geo=row['statut_geo'],
                label_qpv=row['nom_qpv'],
                label_comu=row['commune']
            )
            # Ajouter l'objet à la liste localisations_to_create et marquer son ID comme créé
            localisations_to_create.append(localisation)
            local_ids_created.add(local_id)

    # Parcourir les lignes de la table app_club_2
    for _, row in df_app_club_2.iterrows():
        code_commune = row['code_commune']
        code_qpv = row['code_qpv']
        local_id = code_commune + '-' + code_qpv

        # Vérifier si cette localisation n'a pas déjà été créée
        if local_id not in local_ids_created:
            # Créer un objet D_Localisation avec les données de la ligne actuelle
            localisation = D_Localisation(
                local_id=local_id,
                code_comu=code_commune,
                code_qpv=code_qpv,
                region=row['region'],
                departement=row['departement'],
                statut_geo=row['statut_geo'],
                label_qpv=row['nom_qpv'],
                label_comu=row['commune']
            )
            # Ajouter l'objet à la liste localisations_to_create et marquer son ID comme créé
            localisations_to_create.append(localisation)
            local_ids_created.add(local_id)

    # Créer les objets D_Localisation en une seule opération de base de données
    D_Localisation.objects.bulk_create(localisations_to_create)

    # Fermer la connexion à la base de données
    conn.close()
