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




