# from django.db import models
# from django.conf import settings
# from django.db.models.signals import post_save, post_init, pre_save
# from django.dispatch import receiver
# from django.utils import timezone
# from django.db.models import Sum
# from allauth.account.signals import user_signed_up, user_logged_in
# from django_countries.fields import CountryField
# from datetime import timedelta, date, datetime
# from PIL import Image
# import uuid
# import random, string
# import pyotp


# class RentalGame(models.Model):
#     name = models.CharField(max_length=200)
#     platform = models.CharField(max_length=200)
#     cat = models.CharField(max_length=200)
#     quantity = models.IntegerField(default=1)
#     displayImagePath = models.ImageField(
#         upload_to="vendor/gameon/rental/games/displayImagePath/",
#         default="default_display_pics.jpg",
#         blank=True,
#     )
#     bannerImagePath = models.ImageField(
#         upload_to="vendor/gameon/rental/games/bannerImagePath/",
#         default="default_banner_pics.jpg",
#         blank=True,
#     )
#     thumbnailImagePath = models.ImageField(
#         upload_to="vendor/gameon/rental/games/thumbnailImagePath/",
#         default="default_thumbnail_pics.jpg",
#         blank=True,
#     )
#     dailyRentalRate = models.IntegerField(default=1000)
#     adminOwned = models.BooleanField(default=True)
#     featured = models.BooleanField(default=False)
#     featured_banner = models.BooleanField(default=False)
#     vendor = models.CharField(max_length=200, blank=True, null=True)
#     comingSoon = models.BooleanField(default=False)
#     created_at = models.DateTimeField(default=timezone.now)

#     def __str__(self):
#         return self.name


# class RentalGameTrailer(models.Model):
#     name = models.CharField(max_length=200)
#     platform = models.ForeignKey(
#         "RentalPlatform", related_name="trailer_platform", on_delete=models.CASCADE
#     )
#     trailer_banner = models.ImageField(
#         upload_to="gameon/rental/trailers/bannerImagePath/",
#         default="default_banner_pics.jpg",
#         blank=True,
#     )
#     trailer_file_mp4 = models.FileField(
#         upload_to="gameon/rental/trailers/mp4/",
#         default="default_mp4_trailer.mp4",
#         blank=True,
#     )
#     trailer_file_webm = models.FileField(
#         upload_to="gameon/rental/trailers/mp4/",
#         default="default_webm_trailer.webm",
#         blank=True,
#     )
#     highlight_title = models.CharField(max_length=400, blank=True, null=True)
#     highlight_desc = models.TextField(blank=True, null=True)
#     views = models.IntegerField(default=0)
#     created_at = models.DateTimeField(default=timezone.now)

#     def __str__(self):
#         return self.name
