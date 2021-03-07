from django.contrib.gis import admin
from .models import Post,Postnummer


admin.site.register(Post, admin.OSMGeoAdmin)
admin.site.register(Postnummer,admin.OSMGeoAdmin)

# Register your models here.
