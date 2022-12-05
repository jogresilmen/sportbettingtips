"""uRLs para base
"""
# Django Libraries
# Django Library
from django.conf.urls import include
from django.urls import path

urlpatterns = [
    # ============================ New URLs ============================ #
    path("glosary/", include("app.main.urls.glosary")),
    path("sequence/", include("app.main.urls.sequence")),
    path("dpt/", include("app.main.urls.dpt")),
]
