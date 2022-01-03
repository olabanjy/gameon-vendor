from typing import cast
from django import template
from django.contrib import messages
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import (
    HttpResponse,
    HttpResponseRedirect,
    HttpResponseForbidden,
    HttpResponseServerError,
)
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, reverse, get_object_or_404, redirect
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
from django.db.models import Sum
from django.core.mail import EmailMultiAlternatives, send_mail, EmailMessage
from django.template.loader import render_to_string
from django.template import RequestContext
from django.utils.encoding import force_bytes
import requests
import json
from .models import *


class ItemList(View):
    template = "shop/items.html"

    def get(self, request, *args, **kwargs):

        platform_base_url = "https://gameon-ng.herokuapp.com/api/v1/shop/item/platform/"
        cat_base_url = "https://gameon-ng.herokuapp.com/api/v1/shop/item/cat/"
        type_base_url = "https://gameon-ng.herokuapp.com/api/v1/shop/item/type/"

        platform = requests.get(f"{platform_base_url}")
        plat_list = [sub["name"] for sub in platform.json()]
        print(plat_list)
        cat = requests.get(f"{cat_base_url}")
        cat_list = [sub["name"] for sub in cat.json()]
        print(cat_list)
        type = requests.get(f"{type_base_url}")
        type_list = [sub["name"] for sub in type.json()]
        print(type_list)

        all_ur_items = Item.objects.filter(vendor=self.request.user.profile).all()

        context = {
            "all_ur_items": all_ur_items,
            "platforms": plat_list,
            "cats": cat_list,
            "types": type_list,
        }

        return render(self.request, self.template, context)

    def post(self, request, *args, **kwargs):
        item_name = request.POST.get("item_name")
        displayImagePath = request.FILES["displayImagePath"]
        thumbnailImagePath = request.FILES["thumbnailImagePath"]
        bannerImagePath = request.FILES["bannerImagePath"]
        item_platform = request.POST.get("item_platform")
        item_quantity = request.POST.get("item_quantity")
        item_price = request.POST.get("item_price")
        discount_price = request.POST.get("discount_price")
        item_cat = request.POST.get("item_cat")
        item_type = request.POST.get("item_type")

        new_item = Item.objects.create(
            vendor=self.request.user.profile,
            name=item_name,
            platform=item_platform,
            cat=item_cat,
            type=item_type,
            quantity=item_quantity,
            displayImagePath=displayImagePath,
            thumbnailImagePath=thumbnailImagePath,
            bannerImagePath=bannerImagePath,
            price=item_price,
        )
        if discount_price:
            new_item.discount_price = discount_price

        if "itemTrailerVideo" in request.FILES:
            itemTrailerVideo = request.FILES["itemTrailerVideo"]
            new_item.itemTrailerVideo = itemTrailerVideo

        new_item.save()

        print("item saved")

        return redirect("shop:item-list")
