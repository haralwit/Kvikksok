from django.contrib.gis import admin
from .models import Post,Postnummer,Kvikkleire


admin.site.register(Post, admin.OSMGeoAdmin)
admin.site.register(Postnummer,admin.OSMGeoAdmin)
admin.site.register(Kvikkleire,admin.OSMGeoAdmin)

# Register your models here.
