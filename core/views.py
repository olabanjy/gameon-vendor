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
from users.models import *
import requests, time


@login_required
def dashboard(request):
    if not request.user.profile.profile_set_up:
        return redirect("users:profile-set-up")
    template = "core/dashboard.html"

    rentalOrderCount = 0
    shopOrderCount = 0
    rentalOrderRev = 0
    shopOrderRev = 0

    vendor_code = request.user.profile.vendor_code
    # vendor_code = "OFY57RQA"
    print(vendor_code)
    rental_orders = requests.get(
        f"{settings.CLIENT_BASE_URL}rental/que/get_vendor_orders/?vendor_code={vendor_code}&timestamp={time.time()}"
    )
    if rental_orders.status_code == 200:
        rentalOrderCount = len(rental_orders.json())
        print(rental_orders.json())
        for item in rental_orders.json():
            rentalOrderRev += int(item["item"]["dailyRentalRate"])

    shop_orders = requests.get(
        f"{settings.CLIENT_BASE_URL}shop/item/order/get_vendor_orders/?vendor_code={vendor_code}&timestamp={time.time()}"
    )
    if shop_orders.status_code == 200:
        shopOrderCount = len(shop_orders.json())
        print(shop_orders.json())
        for item in shop_orders.json():
            shopOrderRev += int(item["item"]["price"])

    context = {
        "page_title": "Dashboard",
        "rentalOrderCount": rentalOrderCount,
        "shopOrderCount": shopOrderCount,
        "rentalOrderRev": rentalOrderRev,
        "shopOrderRev": shopOrderRev,
    }

    return render(request, template, context)
