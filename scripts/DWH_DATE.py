import sqlite3
from collections import defaultdict
import pandas as pd
from api.models import D_Date

def run():
    """Importe les données de la table app_date dans le modèle D_Date."""
    conn = sqlite3.connect('db.sqlite3')
    
    df_date = pd.read_sql_query("SELECT * FROM app_club", conn)
    dates_to_create = defaultdict(list)
    
    for _, row in df_date.iterrows():
        insert_date = row['date']
        
        if insert_date not in dates_to_create:
            dates_to_create[insert_date] = D_Date(
                insert_date=insert_date
            )
    
    D_Date.objects.bulk_create(dates_to_create.values())
    
    conn.close()