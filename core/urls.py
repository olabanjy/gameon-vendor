from django.urls import path, include
from .views import *
from django.contrib.auth.decorators import login_required

app_name = "core"


urlpatterns = [
    path("", dashboard, name="dashboard"),
]
