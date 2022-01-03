from django.urls import path, include
from .views import *
from django.contrib.auth.decorators import login_required

app_name = "users"

urlpatterns = [
    # ACCOUNT SET UP AND KYC
    path(
        "profile-set-up/", login_required(SetUpProfile.as_view()), name="profile-set-up"
    ),
]
