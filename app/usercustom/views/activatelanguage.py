# -*- coding: utf-8 -*-
"""
Vistas de la aplicación main
"""

# Standard Libraries
from urllib.parse import urlparse

# Django Libraries
from django.conf import settings
from django.shortcuts import redirect
from django.urls import resolve, reverse
from django.utils import translation
from django.views.generic.base import View
from django.shortcuts import render


# ==================================================================================== #
class ActivateLanguageView(View):
    """ Clase para la activación de un lenguaje
    """

    language_code = ""
    redirect_from = ""
    redirect_to = ""
    match = ""

    def get(self, request, *args, **kwargs):
        """ Metodo para hacer switch en idiomas
        """
        self.redirect_from = request.META.get("HTTP_REFERER", None) or "/"
        self.match = resolve(urlparse(self.redirect_from)[2])
        self.language_code = kwargs.get("language_code")
        if self.match.namespace:
            self.redirect_to = self.match.namespace + ":"
        self.redirect_to += self.match.url_name
        translation.activate(self.language_code)
        response = redirect(reverse(self.redirect_to, kwargs=self.match.kwargs))
        response.set_cookie(settings.LANGUAGE_COOKIE_NAME, self.language_code)
        return response
        