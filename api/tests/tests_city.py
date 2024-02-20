from django.test import TestCase
from rest_framework.test import APIRequestFactory
from rest_framework import status
from api.views import CityAPIView
from api.models import City



class TestCityAPI(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = CityAPIView.as_view()
        self.city_data = {
            'postal_code': '10001',
            'name': 'New York',
            'department': 'New York',
            'region': 'New York',
            'country': 'USA'
        }
        City.objects.create(**self.city_data)

    def test_get_city(self):
        request = self.factory.get('cities/10001/')
        response = self.view(request, postal_code='10001')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['postal_code'], '10001')

    def test_get_nonexistent_city(self):
        request = self.factory.get('cities/99999/')
        response = self.view(request, postal_code='99999')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_create_city(self):
        data = {
            'postal_code': '20000',
            'name': 'Los Angeles',
            'department': 'California',
            'region': 'California',
            'country': 'USA'
        }
        request = self.factory.post('cities/', data)
        response = self.view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(City.objects.filter(postal_code='20000').exists(), True)
        
    def test_patch_city(self):
        data = {'name': 'New Orleans'}
        request = self.factory.patch('cities/10001/', data)
        response = self.view(request, postal_code='10001')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'New Orleans')
        
    def test_put_city(self):
        data = {
            'postal_code': '10001',
            'name': 'Los Angeles',
            'department': 'California',
            'region': 'California',
            'country': 'USA'
        }
        request = self.factory.put('cities/10001/', data)
        response = self.view(request, postal_code='10001')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Los Angeles')

    def test_delete_city(self):
        request = self.factory.delete('cities/10001/')
        response = self.view(request, postal_code='10001')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(City.objects.filter(postal_code='10001').exists(), False)
