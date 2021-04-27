from django.contrib.gis.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.


class Postnummer(models.Model):
    postnummer = models.BigIntegerField()
    poststed = models.CharField(max_length=23)
    geom = models.PointField(srid=4326)

    def __str__(self):
        return str(self.postnummer)


# Auto-generated `LayerMapping` dictionary for postnummer model
postnummer_mapping = {
    'postnummer': 'postnummer',
    'poststed': 'poststed',
    'geom': 'POINT',
}


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    geom = models.PointField(srid=4326) 

    def __str__(self):
        return self.title


class Kvikkleire(models.Model):
    skredomrid = models.BigIntegerField()
    skredomrna = models.CharField(max_length=36)
    arealkm2 = models.FloatField()
    skredfareg = models.CharField(max_length=7)
    skredskade = models.BigIntegerField()
    skredrisik = models.BigIntegerField()
    skredkvalk = models.BigIntegerField()
    geom = models.MultiPolygonField(srid=4326)

    def __str__(self):
        return self.skredomrna


# Auto-generated `LayerMapping` dictionary for Kvikkleire model
kvikkleire_mapping = {
    'skredomrid': 'skredOmrID',
    'skredomrna': 'skredOmrNa',
    'arealkm2': 'arealKm2',
    'skredfareg': 'skredFareg',
    'skredskade': 'skredSkade',
    'skredrisik': 'skredRisik',
    'skredkvalk': 'skredKvalK',
    'geom': 'MULTIPOLYGON',
}
