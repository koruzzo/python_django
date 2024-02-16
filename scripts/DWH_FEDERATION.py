import sqlite3
import pandas as pd
from api.models import D_Federation


def run():
    """Importe les données de la table app_club et app_club_2 dans le modèle D_Federation."""
    conn = sqlite3.connect('db.sqlite3')
    df_app_club = pd.read_sql_query("SELECT * FROM app_club WHERE region = 'Auvergne-Rhône-Alpes' AND code_commune != 'NR - Non réparti'", conn)
    df_app_club_2 = pd.read_sql_query("SELECT * FROM app_club_2 WHERE region = 'Auvergne-Rhône-Alpes' AND code_commune != 'NR - Non réparti'", conn)

    df_app_club_2 = df_app_club_2.loc[:, ~df_app_club_2.columns.str.contains('f_nr|h_nr|nr_nr')]


    fede_objects = []
    fede_ids_created = set()

    for _, row in df_app_club.iterrows():
        fede_code = row['code']
        fede_label = row['federation']
        fede_id = row['code'] + '-' + row['federation']
        if fede_id not in fede_ids_created:
            fede_objects.append(D_Federation(fede_id=fede_id, fede_code=fede_code, fede_label=fede_label))
            fede_ids_created.add(fede_id)

    for _, row in df_app_club_2.iterrows():
        fede_code = row['code']
        fede_label = row['federation']
        fede_id = row['code'] + '-' + row['federation']
        if fede_id not in fede_ids_created:
            fede_objects.append(D_Federation(fede_id=fede_id, fede_code=fede_code, fede_label=fede_label))
            fede_ids_created.add(fede_id)

    D_Federation.objects.bulk_create(fede_objects)

    conn.close()
