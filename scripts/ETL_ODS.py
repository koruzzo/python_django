import pandas as pd
from django.utils import timezone
from app.models import Club
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, 'data')

def run():
    csv_file_path = os.path.join(DATA_DIR, 'clubs-data-2021.csv')  
    df = pd.read_csv(csv_file_path, sep=';')

    clubs_to_create = []
    current_date = timezone.now()
    for _, row in df.iterrows():
        club = Club(
            code_commune=row['Code Commune'],
            commune=row['Commune'],
            code_qpv=row['Code QPV'],
            nom_qpv=row['Nom QPV'],
            departement=row['Département'],
            region=row['Région'],
            statut_geo=row['Statut géo'],
            code=row['Code'],
            federation=row['Fédération'],
            clubs=row['Clubs'],
            epa=row['EPA'],
            total=row['Total'],
            date=current_date
        )
        clubs_to_create.append(club)
    Club.objects.bulk_create(clubs_to_create)
