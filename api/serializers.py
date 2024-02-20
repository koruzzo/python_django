from rest_framework import serializers
from app.models import Club_2, Club
from api.models import D_AgeGrp, D_Date, D_Federation, D_Localisation, D_Sex, D_Type, F_Club, F_Licence, City

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

class CitySerializer(serializers.ModelSerializer):
    """Serializer pour le modèle City."""
    class Meta:
        model = City
        fields = '__all__'

# class FClubSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = F_Club
#         fields = '__all__'

# class FLicenceSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = F_Licence
#         fields = '__all__'
