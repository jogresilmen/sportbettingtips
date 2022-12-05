"""uRLs para base
"""
# Django Libraries
# Django Library
from django.urls import path

# Local Folders Libraries
from ..views import EstadoAutoComplete, MunicipioAutoComplete, ParroquiaAutoComplete

app_name = "dpt"

urlpatterns = [
    # Rutas de Auto Completado de la División Político Territorial Personas #
    path("dpt/estado/", EstadoAutoComplete.as_view(), name="estado"),
    path("dpt/municipio/", MunicipioAutoComplete.as_view(), name="municipio"),
    path("dpt/parroquia/", ParroquiaAutoComplete.as_view(), name="parroquia"),
]
