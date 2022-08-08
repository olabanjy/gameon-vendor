from django import template
from django.contrib import messages
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import (
    HttpResponse,
    HttpResponseRedirect,
    HttpResponseForbidden,
    HttpResponseServerError,
    JsonResponse,
)
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, reverse, get_object_or_404, redirect
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
from django.core.mail import EmailMultiAlternatives, send_mail, EmailMessage
from django.template.loader import render_to_string
from django.template import RequestContext
from django.utils.encoding import force_bytes
from paystackapi.paystack import Paystack
from django.db.models import Sum
from .forms import *
from .models import *

from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
from django.utils.timezone import make_aware

from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
import pandas as pd
import time
import re
import random, string
from decimal import Decimal
from django.contrib.humanize.templatetags.humanize import intcomma


from datetime import timedelta, date, datetime, time
from dateutil.relativedelta import relativedelta


class SetUpProfile(View):
    template = "users/profile_set_up.html"

    def get(self, request, *args, **kwargs):

        if self.request.user.profile.profile_set_up == True:
            return redirect("/")

        form = ProfileSetUpForm()

        context = {"form": form}
        return render(self.request, self.template, context)

    def post(self, request, *args, **kwargs):

        form = ProfileSetUpForm(self.request.POST, self.request.FILES or None)

        try:
            profile = Profile.objects.get(user=self.request.user)

            if form.is_valid():
                first_name = form.cleaned_data.get("first_name")
                last_name = form.cleaned_data.get("last_name")
                phone = form.cleaned_data.get("phone")
                dob = form.cleaned_data.get("dob")
                address_1 = form.cleaned_data.get("address_1")
                address_2 = form.cleaned_data.get("address_2")
                city = form.cleaned_data.get("city")
                state = form.cleaned_data.get("state")
                shop_name = form.cleaned_data.get("shop_name")
                print(phone)

                doc_type = form.cleaned_data.get("doc_type")
                document_front = form.cleaned_data.get("document_front")
                document_back = form.cleaned_data.get("document_back")

                profile.first_name = first_name
                profile.last_name = last_name
                profile.shop_name = shop_name
                profile.phone = phone
                profile.dob = dob

                vendor_address, created = Address.objects.get_or_create(user=profile)

                vendor_address.street_address = address_1
                vendor_address.apartment_address = address_2
                vendor_address.city = city
                vendor_address.state = state
                vendor_address.save()

                vendor_kyc, created = UserKYC.objects.get_or_create(user=profile)

                vendor_kyc.photo = document_front
                vendor_kyc.photo_2 = document_back

                if doc_type == 0:
                    vendor_kyc.id_type = "passport"
                elif doc_type == 1:
                    vendor_kyc.id_type = "driving_license"
                else:
                    vendor_kyc.id_type = "national_id"

                vendor_kyc.save()

                profile.profile_set_up = True
                profile.save()

                # TO DO
                # send_kyc_submitted_email.delay(self.request.user.pk)
                # send_kyc_submitted_email_admin.delay(self.request.user.pk)

                return HttpResponseRedirect(reverse("core:dashboard"))

            else:
                print("Form is not valid")
                print(form.errors)

            return render(self.request, self.template, {"form": form})

        except (ValueError, NameError, TypeError) as error:
            err_msg = str(error)
            print(err_msg)
            return render(self.request, self.template, {"form": form})
        except:
            print("Unexpected Error")
            raise
