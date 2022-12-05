"""sportbettingtips URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import handler404, handler500, include
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path
from django.utils.translation import gettext_lazy as _
from django.views.static import serve
# Thirdparty Libraries
from app.usercustom.views import ActivateLanguageView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("app.main.urls")),
    path("", include("app.usercustom.urls")),
    path("config", include("app.config.urls")),
    path("media/<path:path>", serve, {"document_root": settings.MEDIA_ROOT}),
    path("static/<path:path>", serve, {"document_root": settings.STATIC_ROOT}),
]

urlpatterns += i18n_patterns(
    path("i18n/", include("django.conf.urls.i18n")),
    path(
        "<language_code>/language/activate/",
        ActivateLanguageView.as_view(),
        name="activate_language",
    ),
)

handler404 = "app.usercustom.views.error_404"
handler500 = "app.usercustom.views.error_500"