from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from .views import (
    getSex,
)


app_name = "Config"

urlpatterns = [
    path("sex", getSex.as_view(), name="sex"),
    # path("activate/<uidb64>/<token>", ActivateView.as_view(), name="activar"),
    
]