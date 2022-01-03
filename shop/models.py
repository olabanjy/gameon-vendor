from django.db import models
from django.conf import settings
from django.db.models.signals import post_save, post_init, pre_save
from django.dispatch import receiver
from django.utils import timezone
from django.db.models import Sum
from django.urls import reverse
from allauth.account.signals import user_signed_up, user_logged_in
from django_countries.fields import CountryField
from datetime import timedelta, date, datetime
from PIL import Image
import uuid
import random
import string
import pyotp
from users.models import Address, Profile
from decimal import Decimal

# from users.models import Profile


class Item(models.Model):
    name = models.CharField(max_length=200)
    vendor = models.ForeignKey("users.Profile", on_delete=models.CASCADE)
    platform = models.CharField(max_length=200)
    cat = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    quantity = models.IntegerField(default=1)
    displayImagePath = models.ImageField(
        upload_to="vendor/gameon/shop/items/displayImagePath/",
        default="default_display_pics.jpg",
        blank=True,
    )
    bannerImagePath = models.ImageField(
        upload_to="vendor/gameon/shop/items/bannerImagePath/",
        default="default_banner_pics.jpg",
        blank=True,
    )
    thumbnailImagePath = models.ImageField(
        upload_to="vendor/gameon/shop/items/thumbnailImagePath/",
        default="default_thumbnail_pics.jpg",
        blank=True,
    )
    itemTrailerVideo = models.FileField(
        upload_to="vendor/gameon/shop/items/trailer/mp4/",
        default="default_trailer_video.mp4",
        blank=True,
    )
    price = models.IntegerField()
    discount_price = models.IntegerField(blank=True, null=True)
    admin_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
