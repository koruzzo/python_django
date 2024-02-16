"""..."""
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













    def delete(self, request, format=None):
        """Supprimer une entrée de la table spécifiée."""
        table = request.data.get('table')
        if table not in TABLE_SERIALIZER_MAP:
            return Response({'message': 'Nom de table invalide'}, status=status.HTTP_400_BAD_REQUEST)

        model_class, _ = TABLE_SERIALIZER_MAP[table]
        pk = request.data.get('pk')
        if pk is None:
            return Response({'message': 'Veuillez fournir une clé primaire (pk) pour supprimer une entrée'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            instance = model_class.objects.get(pk=pk)
            instance.delete()
            return Response({'message': 'L\'entrée a été supprimée avec succès'}, status=status.HTTP_200_OK)
        except model_class.DoesNotExist:
            return Response({'message': 'L\'entrée spécifiée n\'existe pas'}, status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, format=None):
        """Modifier partiellement une entrée dans la table spécifiée."""
        table = request.data.get('table')
        if table not in TABLE_SERIALIZER_MAP:
            return Response({'message': 'Nom de table invalide'}, status=status.HTTP_400_BAD_REQUEST)

        model_class, serializer_class = TABLE_SERIALIZER_MAP[table]
        pk = request.data.get('pk')
        if pk is None:
            return Response({'message': 'Veuillez fournir une clé primaire (pk) pour modifier une entrée'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            instance = model_class.objects.get(pk=pk)
            serializer = serializer_class(instance, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except model_class.DoesNotExist:
            return Response({'message': 'L\'entrée spécifiée n\'existe pas'}, status=status.HTTP_404_NOT_FOUND)
        
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
