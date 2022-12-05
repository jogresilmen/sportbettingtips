""" Territorial Political Division Views
"""
# main.py

# Thirdparty Libraries
from dal import autocomplete

# Local Folders Libraries
from ..models import Dpt


# ==================================================================================== #
class EstadoAutoComplete(autocomplete.Select2QuerySetView):
    """Servicio de auto completado para los estado  del modelo
    DivisionPoliticoTerritorial
    """

    def get_queryset(self):
        queryset = Dpt.objects.filter(arbol="root.243")

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
            queryset = Dpt.objects.filter(
                arbol__startswith="root.243",
                division__icontains="Municipio",
                division_padre=estado,
            )
        else:
            queryset = Dpt.objects.filter(
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
            queryset = Dpt.objects.filter(
                arbol__startswith="root.243",
                division__icontains="Parroquia",
                division_padre=municipio,
            )
        else:
            queryset = Dpt.objects.filter(
                arbol__startswith="root.243", division__icontains="Parroquia"
            )
        if self.q:
            queryset = queryset.filter(nombre__icontains=self.q)
        return queryset
