import sqlite3
import pandas as pd
from api.models import D_Localisation

def run():
    """Importe les données des tables app_club et app_club_2 dans le modèle D_Localisation."""
    conn = sqlite3.connect('db.sqlite3')

    
    df_app_club = pd.read_sql_query("SELECT * FROM app_club WHERE region = 'Auvergne-Rhône-Alpes' AND code_commune != 'NR - Non réparti'", conn)
    df_app_club_2 = pd.read_sql_query("SELECT * FROM app_club WHERE region = 'Auvergne-Rhône-Alpes' AND code_commune != 'NR - Non réparti'", conn)

    df_app_club_2 = df_app_club_2.loc[:, ~df_app_club_2.columns.str.contains('f_nr','h_nr','nr_nr')]

    localisations_to_create = []


    for _, row in df_app_club.iterrows():
        code_comu = row['code_commune']
        code_qpv = row['code_qpv']
        local_id = row['code_commune'] + '-' + row['code_qpv'] 


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


    for _, row in df_app_club_2.iterrows():
        code_comu = row['code_commune']
        code_qpv = row['code_qpv']
        local_id = row['code_commune'] + '-' + row['code_qpv']  

       
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


    D_Localisation.objects.bulk_create(localisations_to_create)

    conn.close()
