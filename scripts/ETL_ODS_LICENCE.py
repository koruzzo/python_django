import sqlite3
import pandas as pd
from django.utils.text import slugify
from api.models import F_Licence, D_Sex, D_AgeGrp, D_Federation, D_Localisation

def run():
    """Importe les données des tables app_club et app_club_2 dans la table de fait F_Licence."""
    conn = sqlite3.connect('db.sqlite3')

    # Charger les données de la table app_club avec la condition sur la région
    df_app_club = pd.read_sql_query("SELECT * FROM app_club WHERE region = 'Auvergne-Rhône-Alpes'", conn)

    # Charger les données de la table app_club_2 avec la condition sur la région
    df_app_club_2 = pd.read_sql_query("SELECT * FROM app_club_2 WHERE region = 'Auvergne-Rhône-Alpes'", conn)

    # Créer un dictionnaire pour stocker les objets de clés étrangères
    sex_dict = {sex.sex_code: sex for sex in D_Sex.objects.all()}
    age_dict = {age.age_label: age for age in D_AgeGrp.objects.all()}
    fede_dict = {fede.fede_id: fede for fede in D_Federation.objects.all()}
    local_dict = {local.local_id: local for local in D_Localisation.objects.all()}

    # Traiter les données de la table app_club
    licences_to_create = []

    for _, row in df_app_club.iterrows():
        for col in row.index:
            if col.startswith(('f_', 'h_')):
                sex_code = col[0].upper()
                sex = sex_dict.get(sex_code)
                age_label = col[2:]
                age = age_dict.get(age_label)
                if sex and age:
                    fede_id = row['code'] + '-' + row['federation']  # Garder la valeur comme elle est
                    fede = fede_dict.get(fede_id)
                    local_id = row['code_commune'] + '-' + row['code_qpv']  # Garder la valeur comme elle est
                    local = local_dict.get(local_id)
                    if fede and local:
                        nb_target = row[col]
                        # Ajouter une condition pour éviter les valeurs NULL
                        if nb_target is not None:
                            licence = F_Licence(
                                sex_fk=sex,
                                age_fk=age,
                                fede_fk=fede,
                                local_fk=local,
                                nb_target=nb_target
                            )
                            licences_to_create.append(licence)
                        else:
                            print("Erreur: Valeur NULL détectée pour le nombre cible")
                    else:
                        print("Erreur: Fédération ou Localisation non trouvée pour :", fede_id, local_id)

    # Traiter les données de la table app_club_2
    for _, row in df_app_club_2.iterrows():
        for col in row.index:
            if col.startswith(('f_', 'h_')):
                sex_code = col[0].upper()
                sex = sex_dict.get(sex_code)
                age_label = col[2:]
                age = age_dict.get(age_label)
                if sex and age:
                    fede_id = row['code'] + '-' + row['federation']  # Garder la valeur comme elle est
                    fede = fede_dict.get(fede_id)
                    local_id = row['code_commune'] + '-' + row['code_qpv']  # Garder la valeur comme elle est
                    local = local_dict.get(local_id)
                    if fede and local:
                        nb_target = row[col]
                        # Ajouter une condition pour éviter les valeurs NULL
                        if nb_target is not None:
                            licence = F_Licence(
                                sex_fk=sex,
                                age_fk=age,
                                fede_fk=fede,
                                local_fk=local,
                                nb_target=nb_target
                            )
                            licences_to_create.append(licence)
                        else:
                            print("Erreur: Valeur NULL détectée pour le nombre cible")
                    else:
                        print("Erreur: Fédération ou Localisation non trouvée pour :", fede_id, local_id)

    F_Licence.objects.bulk_create(licences_to_create)

    conn.close()
