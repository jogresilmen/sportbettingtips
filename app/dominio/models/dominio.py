# Django Libraries
from django.db import models
from django.utils.translation import gettext_lazy as _

# Thirdparty Libraries
from ckeditor.fields import RichTextField
from simple_history.models import HistoricalRecords


# #################################################################################### #
class Dominio(models.Model):
    history = HistoricalRecords()
    nombre = models.CharField(verbose_name=_("Domain Name"), max_length=256)
    razon_social = models.CharField(
        verbose_name=_("Domain Business name"), max_length=256
    )

    def __str__(self):
        return "{}".format(self.razon_social)

    class Meta:
        ordering = ["razon_social"]
        verbose_name = _("Domain")
        verbose_name_plural = _("Domains")
