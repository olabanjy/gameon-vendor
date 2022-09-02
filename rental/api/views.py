from rest_framework.views import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework import serializers, status
from rest_framework.decorators import action
import secrets, datetime, pytz
from distutils.util import strtobool

from .serializers import (
    ItemSerializer,
)

from rental.models import RentalGame

from django.core.mail import send_mail, EmailMessage
from django.template.loader import render_to_string
from django.shortcuts import render

from django.conf import settings
from django.shortcuts import render, HttpResponse
from django.http import JsonResponse

from dateutil.relativedelta import relativedelta
from django.utils.timezone import make_aware
from django.utils import datetime_safe, timezone


import requests, json


class ItemsViewSet(ModelViewSet):
    queryset = RentalGame.objects.all()
    serializer_class = ItemSerializer

    def list(self, request):
        serializer = ItemSerializer(
            self.queryset, many=True, context={"request": request}
        )
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(methods=["GET"], detail=False)
    def get_list(self, request):
        all_items = RentalGame.objects.all()

        for val in all_items:
            print(val.name)

        serializer = ItemSerializer(all_items, many=True)

        response = Response(serializer.data, status=status.HTTP_200_OK)
        response["Cache-Control"] = "no-cache"
        return response

    @action(methods=["POST"], detail=False)
    def approve_item(self, request):
        try:
            the_item = RentalGame.objects.get(id=int(request.data["id"]))
            the_item.admin_approved = True
            the_item.save()
            ### send email to vendor to notify
            return Response(
                {"message": [" Item approved "]},
                status=status.HTTP_200_OK,
            )
        except Exception as e:
            return Response({"message": e}, status=status.HTTP_400_BAD_REQUEST)

    @action(methods=["POST"], detail=False)
    def reject_item(self, request):
        try:
            the_item = RentalGame.objects.get(id=int(request.data["id"]))
            the_item.delete()
            ### send email to vendor to notify

            return Response(
                {"message": [" Item deleted "]},
                status=status.HTTP_200_OK,
            )
        except Exception as e:
            return Response({"message": e}, status=status.HTTP_400_BAD_REQUEST)
