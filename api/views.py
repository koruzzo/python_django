"""..."""
from rest_framework.views import APIView
from rest_framework import serializers
from rest_framework.response import Response
# from rest_framework.pagination import PageNumberPagination
from app.models import Club_2, Club
from api.models import D_AgeGrp, D_Date, D_Federation, D_Localisation, D_Sex, D_Type, F_Club, F_Licence

class EndPointDWH(APIView):
    """..."""
    def get(self, request, format=None):
        """..."""
        table = request.GET['table']
        if table == 'club2':
            queryset = Club_2.objects.all()
            nombre_de_lignes = queryset.count()
            # serializer_class = Club2Serializer
        elif table == 'club':
            queryset = Club.objects.all()
            nombre_de_lignes = queryset.count()
            # serializer_class = ClubSerializer
        elif table == 'f_licence':
            queryset = F_Licence.objects.all()
            nombre_de_lignes = queryset.count()
        elif table == 'f_club':
            queryset = F_Club.objects.all()
            nombre_de_lignes = queryset.count()
        elif table == 'd_agegrp':
            queryset = D_AgeGrp.objects.all()
            nombre_de_lignes = queryset.count()
        elif table == 'd_date':
            queryset = D_Date.objects.all()
            nombre_de_lignes = queryset.count()
        elif table == 'd_federation':
            queryset = D_Federation.objects.all()
            nombre_de_lignes = queryset.count()
        elif table == 'd_localisation':
            queryset = D_Localisation.objects.all()
            nombre_de_lignes = queryset.count()
        elif table == 'd_sex':
            queryset = D_Sex.objects.all()
            nombre_de_lignes = queryset.count()
        elif table == 'd_type':
            queryset = D_Type.objects.all()
            nombre_de_lignes = queryset.count()
        else:
            return Response({'message': 'Nom de table invalide'}, status=400)

        # paginator = PageNumberPagination()
        # paginator.page_size = 1
        # paginated_queryset = paginator.paginate_queryset(queryset, request)
        
        # serializer = serializer_class(paginated_queryset, many=True)
        result = {
            'home' : 'http://localhost:8000/admin',
            'message': 'OK',
            'nombre_de_lignes': nombre_de_lignes,
            'nom_de_table': table,
            # 'data': serializer.data,
            # 'next': paginator.get_next_link(),
            # 'previous': paginator.get_previous_link()
        }
        return Response(result)

# class ClubSerializer(serializers.ModelSerializer):
#     """..."""
#     class Meta:
#         """..."""
#         model = Club
#         fields = '__all__'

# class Club2Serializer(serializers.ModelSerializer):
#     """..."""
#     class Meta:
#         """..."""
#         model = Club_2
#         fields = '__all__'
