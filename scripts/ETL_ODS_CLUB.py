import sqlite3
import pandas as pd
from api.models import F_Club, D_Type, D_Date, D_Federation, D_Localisation
from datetime import datetime

def run():
    """Importe les données des tables app_club et app_club_2 dans la table de fait F_Licence."""
    conn = sqlite3.connect('db.sqlite3')

    # Charger les données de la table app_club avec la condition sur la région
    df_app_club = pd.read_sql_query("SELECT * FROM app_club WHERE region = 'Auvergne-Rhône-Alpes'", conn)

    # Créer un dictionnaire pour stocker les objets de clés étrangères
    alltype_dict = {alltype.type_label: alltype for alltype in D_Type.objects.all()}
    date_dict = {date.insert_date.strftime('%Y-%m-%d'): date for date in D_Date.objects.all()}
    fede_dict = {fede.fede_id: fede for fede in D_Federation.objects.all()}
    local_dict = {local.local_id: local for local in D_Localisation.objects.all()}

    # Traiter les données de la table app_club
    clubs_to_create = []

    for _, row in df_app_club.iterrows():
        fede_id = row['code'] + '-' + row['federation']
        local_id = row['code_commune'] + '-' + row['code_qpv']
        insert_date_str = row['date']  # Récupérer la date en tant que chaîne de caractères

        try:
            # Convertir la chaîne de caractères en objet datetime
            insert_date = datetime.strptime(insert_date_str, '%Y-%m-%d')
            # Utiliser strftime pour formater la date en tant que clé de recherche
            date_key = insert_date.strftime('%Y-%m-%d')
            date = date_dict[date_key]
            fede = fede_dict[fede_id]
            local = local_dict[local_id]
        except KeyError as e:
            print(f"Erreur lors de la récupération des données: {e}")
            continue
        except ValueError as e:
            print(f"Erreur lors de la conversion de la date: {e}")
            continue

        if fede and local and date:
            for col in row.index:
                if col == 'clubs' or col == 'epa':
                    type_label = col
                    alltype = alltype_dict.get(type_label)
                    nb_target = row[col]
                    if nb_target is not None:
                        club = F_Club(
                            date_fk=date,
                            type_fk=alltype,
                            fede_fk=fede,
                            local_fk=local,
                            nb_target=nb_target
                        )
                        clubs_to_create.append(club)
                    else:
                        print("Erreur: Valeur NULL détectée pour le nombre cible")
        else:
            print("Erreur: Fédération ou Localisation non trouvée pour :", fede_id, local_id)

    F_Club.objects.bulk_create(clubs_to_create)

    conn.close()
