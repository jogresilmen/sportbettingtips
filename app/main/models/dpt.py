"""
Modelo de datos de la app main
"""
# Future Libraries
from __future__ import unicode_literals

# Django Libraries
from django.db import models


# ==================================================================================== #
class Dpt(models.Model):
    """Modelo que sirve para gestionar las dicisiones político  territoriales
    de los paises del mundo.
    """

    division = models.CharField(max_length=255, blank=True, null=True)
    nombre = models.CharField(max_length=255, blank=True, null=True)
    division_padre = models.ForeignKey(
        "self", on_delete=models.PROTECT, blank=True, null=True
    )
    arbol = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "División político territorial"
        verbose_name_plural = "División político territorial"
