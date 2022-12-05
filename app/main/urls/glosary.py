"""uRLs para base
"""
# Django Libraries
# Django Library
from django.conf.urls import include
from django.urls import path
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

# Local Folders Libraries
from ..models import Glosary

app_name = "Glosary"

urlpatterns = [
    # ============================ New URLs ============================ #
    path(
        "documentacion/Glosary",
        ListView.as_view(model=Glosary, template_name="Glosary.html"),
        name="Glosary",
    ),
    path(
        "documentacion/Glosary/termino/<int:pk>",
        DetailView.as_view(model=Glosary, template_name="termino.html"),
        name="termino",
    ),
]
