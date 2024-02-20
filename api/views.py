"""..."""
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
# from rest_framework.generics import get_object_or_404
from app.models import Club_2, Club
from api.models import D_AgeGrp, D_Date, D_Federation, D_Localisation, D_Sex, D_Type, F_Club, F_Licence, City
from .serializers import (ClubSerializer, Club2Serializer, FLicenceSerializer, FClubSerializer, DAgeGrpSerializer, DDateSerializer, DFederationSerializer, DLocalisationSerializer, DSexSerializer, DTypeSerializer, CitySerializer)

TABLE_SERIALIZER_MAP = {
    'club2': (Club_2, Club2Serializer),
    'club': (Club, ClubSerializer),
    'f_licence': (F_Licence, FLicenceSerializer),
    'f_club': (F_Club, FClubSerializer),
    'd_agegrp': (D_AgeGrp, DAgeGrpSerializer),
    'd_date': (D_Date, DDateSerializer),
    'd_federation': (D_Federation, DFederationSerializer),
    'd_localisation': (D_Localisation, DLocalisationSerializer),
    'd_sex': (D_Sex, DSexSerializer),
    'd_type': (D_Type, DTypeSerializer),
}

class EndPointDWH(APIView):
    """..."""
    def get(self, request, format=None):
        """Récupérer les données de la table spécifiée."""
        table = request.GET.get('table')
        if table not in TABLE_SERIALIZER_MAP:
            return Response({'message': 'Nom de table invalide'}, status=status.HTTP_400_BAD_REQUEST)

        model_class, serializer_class = TABLE_SERIALIZER_MAP[table]
        queryset = model_class.objects.all()
        nombre_de_lignes = queryset.count()

        paginator = PageNumberPagination()
        paginator.page_size = 1
        paginated_queryset = paginator.paginate_queryset(queryset, request)
        
        serializer = serializer_class(paginated_queryset, many=True)
        result = {
            'home' : 'http://localhost:8000/admin',
            'nombre_de_lignes': nombre_de_lignes,
            'nom_de_table': table,
            'data': serializer.data,
            'next': paginator.get_next_link(),
            'previous': paginator.get_previous_link()
        }
        return Response(result, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        """Insérer une nouvelle entrée dans la table spécifiée."""
        table = request.data.get('table')
        if table not in TABLE_SERIALIZER_MAP:
            return Response({'message': 'Nom de table invalide'}, status=status.HTTP_400_BAD_REQUEST)
        model_class, serializer_class = TABLE_SERIALIZER_MAP[table]
        serializer = serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class D_Sex_DWH(APIView):
#     """..."""

#     lookup_field = 'sex_code'

#     def get(self, request, sex_code=None, format=None):
#         """..."""
#         if sex_code is not None:
#             data = D_Sex.objects.filter(sex_code=sex_code)
#             serializer = DSexSerializer(data, many=True)
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         else:
#             d_sex_instances = D_Sex.objects.all()
#             serializer = DSexSerializer(d_sex_instances, many=True)
#             return Response(serializer.data, status=status.HTTP_200_OK)


class CityAPIView(APIView):
    serializer_class = CitySerializer

    def get(self, request, postal_code=None):
        if postal_code:
            try:
                city = City.objects.get(postal_code=postal_code)
                serializer = CitySerializer(city)
                return Response(serializer.data)
            except City.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            cities = City.objects.all()
            serializer = CitySerializer(cities, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, postal_code):
        try:
            city = City.objects.get(postal_code=postal_code)
        except City.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = CitySerializer(city, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, postal_code):
        try:
            city = City.objects.get(postal_code=postal_code)
            city.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except City.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
