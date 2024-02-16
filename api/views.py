"""..."""
from rest_framework.views import APIView
from rest_framework import serializers
from rest_framework import status
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from app.models import Club_2, Club
from api.models import D_AgeGrp, D_Date, D_Federation, D_Localisation, D_Sex, D_Type, F_Club, F_Licence

class EndPointDWH(APIView):
    """..."""
    def get(self, request, format=None):
        """..."""
        table = request.GET['table']
        if table == 'club2':
            queryset = Club_2.objects.all()
            serializer_class = Club2Serializer
            nombre_de_lignes = queryset.count()
        elif table == 'club':
            queryset = Club.objects.all()
            serializer_class = ClubSerializer
            nombre_de_lignes = queryset.count()
        elif table == 'f_licence':
            queryset = F_Licence.objects.all()
            serializer_class = FLicenceSerializer
            nombre_de_lignes = queryset.count()
        elif table == 'f_club':
            queryset = F_Club.objects.all()
            serializer_class = FClubSerializer
            nombre_de_lignes = queryset.count()
        elif table == 'd_agegrp':
            queryset = D_AgeGrp.objects.all()
            serializer_class = DAgeGrpSerializer
            nombre_de_lignes = queryset.count()
        elif table == 'd_date':
            queryset = D_Date.objects.all()
            serializer_class = DDateSerializer
            nombre_de_lignes = queryset.count()
        elif table == 'd_federation':
            queryset = D_Federation.objects.all()
            serializer_class = DFederationSerializer
            nombre_de_lignes = queryset.count()
        elif table == 'd_localisation':
            queryset = D_Localisation.objects.all()
            serializer_class = DLocalisationSerializer
            nombre_de_lignes = queryset.count()
        elif table == 'd_sex':
            queryset = D_Sex.objects.all()
            serializer_class = DSexSerializer
            nombre_de_lignes = queryset.count()
        elif table == 'd_type':
            queryset = D_Type.objects.all()
            serializer_class = DTypeSerializer
            nombre_de_lignes = queryset.count()
        else:
            return Response({'message': 'Nom de table invalide'}, status=400)

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

class ClubSerializer(serializers.ModelSerializer):
    """..."""
    class Meta:
        """..."""
        model = Club
        fields = '__all__'

class Club2Serializer(serializers.ModelSerializer):
    """..."""
    class Meta:
        """..."""
        model = Club_2
        fields = '__all__'

class FLicenceSerializer(serializers.ModelSerializer):
    """Serializer pour le modèle F_Licence."""
    class Meta:
        model = F_Licence
        fields = '__all__'

class FClubSerializer(serializers.ModelSerializer):
    """Serializer pour le modèle F_Club."""
    class Meta:
        model = F_Club
        fields = '__all__'

class DAgeGrpSerializer(serializers.ModelSerializer):
    """Serializer pour le modèle D_AgeGrp."""
    class Meta:
        model = D_AgeGrp
        fields = '__all__'

class DDateSerializer(serializers.ModelSerializer):
    """Serializer pour le modèle D_Date."""
    class Meta:
        model = D_Date
        fields = '__all__'

class DFederationSerializer(serializers.ModelSerializer):
    """Serializer pour le modèle D_Federation."""
    class Meta:
        model = D_Federation
        fields = '__all__'

class DLocalisationSerializer(serializers.ModelSerializer):
    """Serializer pour le modèle D_Localisation."""
    class Meta:
        model = D_Localisation
        fields = '__all__'

class DSexSerializer(serializers.ModelSerializer):
    """Serializer pour le modèle D_Sex."""
    class Meta:
        model = D_Sex
        fields = '__all__'

class DTypeSerializer(serializers.ModelSerializer):
    """Serializer pour le modèle D_Type."""
    class Meta:
        model = D_Type
        fields = '__all__'