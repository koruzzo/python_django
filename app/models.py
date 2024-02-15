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


class Club_2(models.Model):
    code_commune = models.CharField(max_length=500)
    commune = models.CharField(max_length=500)
    code_qpv = models.CharField(max_length=500)
    nom_qpv = models.CharField(max_length=500)
    departement = models.CharField(max_length=500)
    region = models.CharField(max_length=500)
    statut_geo = models.CharField(max_length=500)
    code = models.CharField(max_length=500)
    federation = models.CharField(max_length=500)
    f_1_4_ans = models.CharField(max_length=500)
    f_5_9_ans = models.CharField(max_length=500)
    f_10_14_ans = models.CharField(max_length=500)
    f_15_19_ans = models.CharField(max_length=500)
    f_20_24_ans = models.CharField(max_length=500)
    f_25_29_ans = models.CharField(max_length=500)
    f_30_34_ans = models.CharField(max_length=500)
    f_35_39_ans = models.CharField(max_length=500)
    f_40_44_ans = models.CharField(max_length=500)
    f_45_49_ans = models.CharField(max_length=500)
    f_50_54_ans = models.CharField(max_length=500)
    f_55_59_ans = models.CharField(max_length=500)
    f_60_64_ans = models.CharField(max_length=500)
    f_65_69_ans = models.CharField(max_length=500)
    f_70_74_ans = models.CharField(max_length=500)
    f_75_79_ans = models.CharField(max_length=500)
    f_80_99_ans = models.CharField(max_length=500)
    f_nr = models.CharField(max_length=500)
    h_1_4_ans = models.CharField(max_length=500)
    h_5_9_ans = models.CharField(max_length=500)
    h_10_14_ans = models.CharField(max_length=500)
    h_15_19_ans = models.CharField(max_length=500)
    h_20_24_ans = models.CharField(max_length=500)
    h_25_29_ans = models.CharField(max_length=500)
    h_30_34_ans = models.CharField(max_length=500)
    h_35_39_ans = models.CharField(max_length=500)
    h_40_44_ans = models.CharField(max_length=500)
    h_45_49_ans = models.CharField(max_length=500)
    h_50_54_ans = models.CharField(max_length=500)
    h_55_59_ans = models.CharField(max_length=500)
    h_60_64_ans = models.CharField(max_length=500)
    h_65_69_ans = models.CharField(max_length=500)
    h_70_74_ans = models.CharField(max_length=500)
    h_75_79_ans = models.CharField(max_length=500)
    h_80_99_ans = models.CharField(max_length=500)
    h_nr = models.CharField(max_length=500)
    nr_nr = models.CharField(max_length=500)
    total = models.CharField(max_length=500)
    # date = models.DateField(default=timezone.now)

    def __str__(self):
        return  f"{self.federation} - {self.commune} - {self.region}"