import requests
from django.conf import settings

url = f"{getattr(settings, 'DOMAIN', '')}:{getattr(settings, 'PORT', '')}/cities/"
api_key = getattr(settings, 'API_KEY', '')
headers = {'Authorization': f'Token {api_key}'}
response = requests.get(url, headers=headers)
if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Erreur lors de la requête : {response.status_code} - {response.reason}")
