import pandas as pd
import googlemaps
import os
from django.conf import settings

gmaps = googlemaps.Client(key=getattr(settings, 'GOOGLE_MAPS_API_KEY', None))
file_path = os.path.join(os.getcwd(), 'data', 'departement.csv')

data = pd.read_csv(file_path, delimiter=',', dtype=str)

def run():
    def geocode_location(address):
        try:
            geocode_result = gmaps.geocode(address)
            if geocode_result and geocode_result[0]['geometry'] and geocode_result[0]['geometry']['location']:
                location = geocode_result[0]['geometry']['location']
                return location['lat'], location['lng']
        except Exception as e:
            print("Erreur lors de la géocodification de l'adresse", address, ":", e)
        return None, None

    data['Latitude'], data['Longitude'] = zip(*data['commune'].apply(geocode_location))

    print(data)

if __name__ == "__main__":
    run()