"""..."""
from django.db import models
from django.utils import timezone

class Player(models.Model):
    """..."""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    def str(self,):
        """..."""
        return f"{self.first_name} - {self.last_name}"

class Club(models.Model):
    """..."""
    code_commune = models.CharField(max_length=10)
    commune = models.CharField(max_length=255)
    code_qpv = models.CharField(max_length=10)
    nom_qpv = models.CharField(max_length=255)
    departement = models.CharField(max_length=10)
    region = models.CharField(max_length=255)
    statut_geo = models.CharField(max_length=255)
    code = models.CharField(max_length=10)
    federation = models.CharField(max_length=255)
    clubs = models.CharField(max_length=10)
    epa = models.CharField(max_length=10)
    total = models.CharField(max_length=10)
    date = models.DateField(default=timezone.now)
    def __str__(self):
        """..."""
        return f"{self.federation} - {self.commune} - {self.date}"
