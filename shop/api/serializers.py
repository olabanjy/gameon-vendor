from rest_framework import serializers
from django.conf import settings
import importlib

from shop.models import Item

from users.models import Address, Profile
from users.api.serializers import ProfileSerializer
from django.contrib.humanize.templatetags.humanize import naturalday


class ItemSerializer(serializers.ModelSerializer):
    vendor = ProfileSerializer()

    class Meta:
        model = Item
        fields = "__all__"
