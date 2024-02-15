"""..."""
from django.db import models
from django.utils.text import slugify

class D_Sex(models.Model):
    """Table de dimension pour le type de sexe."""
    sex_code = models.CharField(primary_key=True, max_length=1)  # M or F

class D_AgeGrp(models.Model):
    """Table de dimension pour les groupes d'âge."""
    age_label = models.CharField(primary_key=True, max_length=20)  # e.g., "15 à 20 ans, ..."

class D_Date(models.Model):
    """Table de dimension pour les dates d'insertion."""
    insert_date = models.DateField(primary_key=True) # Only for F_Club

class D_Type(models.Model):
    """Table de dimension pour le type."""
    type_label = models.CharField(primary_key=True, max_length=5)  # e.g., "Club, EPA"



class D_Federation(models.Model):
    """Table de dimension pour les fédérations."""
    fede_id = models.SlugField(primary_key=True, editable=False, max_length=210)    
    fede_code = models.PositiveIntegerField()
    fede_label = models.CharField(max_length=100)  # Le nom des fédérations

    def save(self, *args, **kwargs):
        # Générer l'identifiant fede_id en concaténant fede_code et fede_label
        self.fede_id = slugify(f"{self.fede_code}-{self.fede_label}")
        super().save(*args, **kwargs)



class D_Localisation(models.Model):
    """Table de dimension pour la localisation."""
    local_id = models.SlugField(primary_key=True, max_length=200)
    code_comu = models.CharField(max_length=8)  # Code de la commune (8 chiffres max)
    code_qpv = models.CharField(max_length=5)  # Code QPV (5 caractères max)
    region = models.CharField(max_length=100)  # Nom de la région
    departement = models.CharField(max_length=100)  # Nom du département
    statut_geo = models.CharField(max_length=100)  # Statut géographique
    label_qpv = models.CharField(max_length=100)  # Nom du QPV
    label_comu = models.CharField(max_length=100)  # Nom de la commune
    
    def save(self, *args, **kwargs):
        # Générer l'identifiant local_id en concaténant code_comu et code_qpv
        self.local_id = slugify(f"{self.code_comu}-{self.code_qpv}")
        super().save(*args, **kwargs)



class F_Licence(models.Model):
    """Table de fait pour les licences."""
    sex_fk = models.ForeignKey('D_Sex', on_delete=models.CASCADE)  # Clé étrangère vers D_Sex
    age_fk = models.ForeignKey('D_AgeGrp', on_delete=models.CASCADE)  # Clé étrangère vers D_AgeGrp
    fede_fk = models.ForeignKey('D_Federation', on_delete=models.CASCADE)  # Clé étrangère vers D_Federation
    local_fk = models.ForeignKey('D_Localisation', on_delete=models.CASCADE)  # Clé étrangère vers D_Localisation
    nb_target = models.PositiveIntegerField()  # Nombre cible



class F_Club(models.Model):
    """Table de fait pour les clubs."""
    fede_fk = models.ForeignKey('D_Federation', on_delete=models.CASCADE)  # Clé étrangère vers D_Federation
    local_fk = models.ForeignKey('D_Localisation', on_delete=models.CASCADE)  # Clé étrangère vers D_Localisation
    date_fk = models.ForeignKey('D_Date', on_delete=models.CASCADE)  # Clé étrangère vers D_Date
    type_fk = models.ForeignKey('D_Type', on_delete=models.CASCADE)  # Clé étrangère vers D_Type
    nb_target = models.PositiveIntegerField()  # Nombre cible