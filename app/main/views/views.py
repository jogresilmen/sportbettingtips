# Librerias Django
# Django Libraries
from django.db.models import Q
from django.http import HttpResponse
from django.template import loader

# Thirdparty Libraries
from dal import autocomplete

# Own Libraries
# Librerias desarrolladas por mi
from flock.models import Flock
from main.models import DivisionPoliticoTerritorial, Taxonomy


# ==================================================================================== #
class EstadoAutoComplete(autocomplete.Select2QuerySetView):
    """Servicio de auto completado para los estado  del modelo
    DivisionPoliticoTerritorial
    """

    def get_queryset(self):
        queryset = DivisionPoliticoTerritorial.objects.filter(arbol="root.243")

        if self.q:
            queryset = queryset.filter(nombre__icontains=self.q)

        return queryset


# ==================================================================================== #
class MunicipioAutoComplete(autocomplete.Select2QuerySetView):
    """Servicio de auto completado para los municipios del modelo
    DivisionPoliticoTerritorial
    """

    def get_queryset(self):

        estado = self.forwarded.get("estado", None)

        if estado:
            queryset = DivisionPoliticoTerritorial.objects.filter(
                arbol__startswith="root.243",
                division__icontains="Municipio",
                division_padre=estado,
            )
        else:
            queryset = DivisionPoliticoTerritorial.objects.filter(
                arbol__startswith="root.243", division__icontains="Municipio"
            )

        if self.q:
            queryset = queryset.filter(nombre__icontains=self.q)

        return queryset


# ==================================================================================== #
class ParroquiaAutoComplete(autocomplete.Select2QuerySetView):
    """Servicio de auto completado para las parroquias del modelo
    DivisionPoliticoTerritorial
    """

    def get_queryset(self):

        municipio = self.forwarded.get("municipio", None)

        if municipio:
            queryset = DivisionPoliticoTerritorial.objects.filter(
                arbol__startswith="root.243",
                division__icontains="Parroquia",
                division_padre=municipio,
            )
        else:
            queryset = DivisionPoliticoTerritorial.objects.filter(
                arbol__startswith="root.243", division__icontains="Parroquia"
            )

        if self.q:
            queryset = queryset.filter(nombre__icontains=self.q)

        return queryset


# ==================================================================================== #
class SubEspecieAutoComplete(autocomplete.Select2QuerySetView):
    """Servicio de auto completado para el modelo Taxonomy (sub especie)
    """

    def get_queryset(self):

        queryset = Taxonomy.objects.filter(clado=100).order_by("otro")

        if self.q:
            queryset = queryset.filter(otro__icontains=self.q)

        return queryset


# ==================================================================================== #
class GrupoRacialAutoComplete(autocomplete.Select2QuerySetView):
    """Servicio de auto completado para el modelo Taxonomy (grupo racial)
    """

    def get_queryset(self):

        print("Aqui voy: %s" % self.forwarded.get("clado_superior", None))
        clado_superior = self.forwarded.get("clado_superior", None)

        queryset = Taxonomy.objects.filter(
            clado=105, clado_superior=clado_superior
        ).order_by("otro")

        if self.q:
            queryset = queryset.filter(otro__icontains=self.q)

        return queryset
