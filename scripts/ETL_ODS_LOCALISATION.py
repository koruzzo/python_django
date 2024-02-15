import sqlite3
import pandas as pd
from api.models import D_Localisation

def run():
    """Importe les données des tables app_club et app_club_2 dans le modèle D_Localisation."""
    conn = sqlite3.connect('db.sqlite3')

    # Charger les données des deux tables app_club et app_club_2 avec la condition sur la région
    df_app_club = pd.read_sql_query("SELECT * FROM app_club WHERE region = 'Auvergne-Rhône-Alpes'", conn)
    df_app_club_2 = pd.read_sql_query("SELECT * FROM app_club_2 WHERE region = 'Auvergne-Rhône-Alpes'", conn)

    localisations_to_create = []

    # Traiter les données de la table app_club
    for _, row in df_app_club.iterrows():
        code_comu = row['code_commune']
        code_qpv = row['code_qpv']
        local_id = row['code_commune'] + '-' + row['code_qpv']  # Générer l'identifiant local_id

        # Vérifier si un enregistrement avec le même local_id existe déjà dans la liste à créer
        if not any(local.local_id == local_id for local in localisations_to_create):
            localisation = D_Localisation(
                local_id=local_id,
                code_comu=code_comu,
                code_qpv=code_qpv,
                region=row['region'],
                departement=row['departement'],
                statut_geo=row['statut_geo'],
                label_qpv=row['nom_qpv'],
                label_comu=row['commune']
            )
            localisations_to_create.append(localisation)

    # Traiter les données de la table app_club_2
    for _, row in df_app_club_2.iterrows():
        code_comu = row['code_commune']
        code_qpv = row['code_qpv']
        local_id = row['code_commune'] + '-' + row['code_qpv']  # Générer l'identifiant local_id

        # Vérifier si un enregistrement avec le même local_id n'existe pas déjà dans la liste à créer
        if not any(local.local_id == local_id for local in localisations_to_create):
            localisation = D_Localisation(
                local_id=local_id,
                code_comu=code_comu,
                code_qpv=code_qpv,
                region=row['region'],
                departement=row['departement'],
                statut_geo=row['statut_geo'],
                label_qpv=row['nom_qpv'],
                label_comu=row['commune']
            )
            localisations_to_create.append(localisation)

    # Insérer les localisations dans la base de données
    D_Localisation.objects.bulk_create(localisations_to_create)

    conn.close()
