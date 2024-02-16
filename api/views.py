from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from app.models import Club_2, Club
from api.models import D_AgeGrp, D_Date, D_Federation, D_Localisation, D_Sex, D_Type, F_Club, F_Licence
from .serializers import (ClubSerializer, Club2Serializer, FLicenceSerializer, FClubSerializer, DAgeGrpSerializer, DDateSerializer, DFederationSerializer, DLocalisationSerializer, DSexSerializer, DTypeSerializer)

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
        """..."""
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