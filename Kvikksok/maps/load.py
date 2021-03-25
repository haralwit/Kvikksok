from pathlib import Path
from django.contrib.gis.utils import LayerMapping
from .models import Kvikkleire,kvikkleire_mapping



shape_shp = Path(__file__).resolve().parent / 'data' / 'kvikkleire.shp'

def run(verbose=True):
    lm = LayerMapping(Kvikkleire, str(shape_shp), kvikkleire_mapping, transform=False)
    lm.save(strict=True, verbose=verbose)