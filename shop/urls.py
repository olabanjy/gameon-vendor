from django.urls import path, include
from .views import *
from django.contrib.auth.decorators import login_required

app_name = "shop"

urlpatterns = [
    path("item-list/", login_required(ItemList.as_view()), name="item-list"),
]
