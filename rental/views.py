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
    template = "rental/rental_items.html"

    def get(self, request, *args, **kwargs):

        # platform_base_url = "https://gameon-ng.herokuapp.com/api/v1/shop/item/platform/"
        # cat_base_url = "https://gameon-ng.herokuapp.com/api/v1/shop/item/cat/"

        cat_base_url = f"{settings.CLIENT_BASE_URL}rental/cat/"

        cat = requests.get(f"{cat_base_url}")
        cat_list = [sub["name"] for sub in cat.json()]
        print(cat_list)

        all_ur_items = RentalGame.objects.filter(vendor=self.request.user.profile).all()

        context = {
            "all_ur_items": all_ur_items,
            "cats": cat_list,
        }

        return render(self.request, self.template, context)

    def post(self, request, *args, **kwargs):
        if self.request.user.profile.onboarded == False:
            print("You cannot add products yet ")
            return redirect("rental:item-list")

        item_name = request.POST.get("item_name")
        item_desc = request.POST.get("item_desc")
        displayImagePath = request.FILES["displayImagePath"]
        thumbnailImagePath = request.FILES["thumbnailImagePath"]
        bannerImagePath = request.FILES["bannerImagePath"]

        numberInStock = request.POST.get("numberInStock")
        dailyRentalRate = request.POST.get("dailyRentalRate")

        item_cat = request.POST.get("item_cat")

        new_item = RentalGame.objects.create(
            vendor=self.request.user.profile,
            name=item_name,
            cat=item_cat,
            desc=item_desc,
            numberInStock=numberInStock,
            displayImagePath=displayImagePath,
            thumbnailImagePath=thumbnailImagePath,
            bannerImagePath=bannerImagePath,
            dailyRentalRate=dailyRentalRate,
        )

        new_item.save()

        # send nudge to super admin to approve

        print("item saved")

        return redirect("rental:item-list")


class ItemDetail(View):
    def get(self, request, item_id, *args, **kwargs):

        the_game = RentalGame.objects.filter(id=item_id).first()
        template = "rental/rental_item_details.html"

        cat_base_url = f"{settings.CLIENT_BASE_URL}rental/cat/"

        cat = requests.get(f"{cat_base_url}")
        cat_list = [sub["name"] for sub in cat.json()]
        print(cat_list)

        context = {
            "page_title": "Rental Items Details",
            "the_game": the_game,
            "cats": cat_list,
        }

        return render(self.request, template, context)

    def post(self, request, item_id, *args, **kwargs):
        try:

            item_name = request.POST.get("item_name")
            numberInStock = request.POST.get("numberInStock")
            dailyRentalRate = request.POST.get("dailyRentalRate")

            desc = request.POST.get("item_desc")

            the_game = RentalGame.objects.filter(id=item_id).first()

            print(the_game)

            if item_name:
                the_game.name = item_name

            if numberInStock:
                the_game.numberInStock = numberInStock

            if dailyRentalRate:
                the_game.dailyRentalRate = dailyRentalRate

            if desc:
                the_game.desc = desc

            if "displayImagePath" in request.FILES:
                the_game.displayImagePath = request.FILES["displayImagePath"]
                # response_files.append(
                #     ("displayImagePath", request.FILES["displayImagePath"].file)
                # )
            if "thumbnailImagePath" in request.FILES:
                the_game.thumbnailImagePath = request.FILES["thumbnailImagePath"]

            if "bannerImagePath" in request.FILES:
                the_game.bannerImagePath = request.FILES["bannerImagePath"]

            the_game.save()

            return redirect(reverse("rental:item-details", kwargs={"item_id": item_id}))
        except Exception as e:
            print(e)
            return redirect(reverse("rental:item-details", kwargs={"item_id": item_id}))


def delete_item(request, item_id):
    try:
        the_game = RentalGame.objects.get(id=item_id)
        the_game.delete()
        return redirect("rental:item-list")

    except Exception as e:
        print(e)
        return redirect("rental:item-list")


# import time


# @login_required
# def my_shop_orders(request):
#     template = "shop/shop_orders.html"
#     vendor_code = request.user.profile.vendor_code
#     orders = requests.get(
#         f"{settings.CLIENT_BASE_URL}shop/item/order/get_vendor_orders/?vendor_code={vendor_code}&timestamp={time.time()}"
#     )
#     print(orders.json())
#     context = {"orders": orders.json()}
#     return render(request, template, context)


# # @login_required
# # def shop_order_details(request, order_id):
# #     template = "shop/shop_order_details.html"
# #     order = requests.get(f"{settings.CLIENT_BASE_URL}shop/item/order/{order_id}")
# #     context = {"order": order.json()}
# #     return render(request, template, context)
