from pathlib import Path
from django.contrib.gis.utils import LayerMapping
from .models import Postnummer,postnummer_mapping



postnummer_shp = Path(__file__).resolve().parent / 'data' / 'postnummer.shp'

def run(verbose=True):
    lm = LayerMapping(Postnummer, str(postnummer_shp), postnummer_mapping, transform=False)
    lm.save(strict=True, verbose=verbose)