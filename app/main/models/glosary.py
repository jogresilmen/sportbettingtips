"""
Modelo de datos de la app main
"""
# Django Libraries
from django.db import models
from django.utils.translation import gettext_lazy as _

# Thirdparty Libraries
from ckeditor.fields import RichTextField
from simple_history.models import HistoricalRecords


# ==================================================================================== #
class Glosary(models.Model):
    """
    Modelo administrativo: Almacena la definición de los terminos utilizados en
    FincaSoft
    """

    history = HistoricalRecords()
    term = models.CharField(max_length=255, verbose_name=_("Term"))
    description = RichTextField(verbose_name=_("Description"))

    def __str__(self):
        return self.term

    class Meta:
        verbose_name = _("Term")
        verbose_name_plural = _("Glosary")
