import requests
from django.conf import settings
from api.models import D_Localisation

class Geocoding:

    def get_departement(self, value):
        url = 'https://maps.googleapis.com/maps/api/geocode/json'
        params = {
            'key': getattr(settings, 'GOOGLE_MAPS_API_KEY', ''),
            'address': value
        }

        result = requests.get(url, params=params)
        data = result.json()

        if 'results' in data and data['results']:
            address_components = data['results'][0]['address_components']
            if len(address_components) >= 2:
                return address_components[1]['long_name']

        return "Département non trouvé"

def run():
    geo = Geocoding()
    localisations = D_Localisation.objects.values_list('local_id', 'code_comu', 'label_comu').distinct()
    for local_id, code_comu, label_comu in localisations:
        value = f"{code_comu} - {label_comu}"
        department = geo.get_departement(value)
        print(f"Code commune: {code_comu}, Commune: {label_comu}, Département: {department}")

        instance = D_Localisation.objects.get(local_id=local_id)
        instance.nom_departement = department
        instance.save()
