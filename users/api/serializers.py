from ast import Add
from rest_framework import serializers
from django.conf import settings
import importlib


from users.models import Address, Profile, UserKYC, UserBankAccount
from django.contrib.humanize.templatetags.humanize import naturalday


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = [
            "street_address",
            "apartment_address",
            "city",
            "state",
            "zip",
            "long",
            "lat",
        ]


class BankAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserBankAccount
        fields = [
            "account_number",
            "account_name",
            "account_bank",
            "account_bank_code",
        ]


class ProfileKYCSerializer(serializers.ModelSerializer):
    time_created = serializers.SerializerMethodField()
    time_verified = serializers.SerializerMethodField()

    class Meta:
        model = UserKYC
        fields = [
            "id",
            "id_type",
            "id_unique_number",
            "photo",
            "photo_2",
            "verified",
            "verified_at",
            "created_at",
            "time_created",
            "time_verified",
        ]

    def get_time_created(self, object):
        created_at = object.created_at
        time_delta = created_at.strftime("%Y-%m-%d %H:%M")
        return time_delta

    def get_time_verified(self, object):

        verified_at = (
            None
            if object.verified_at is None
            else object.verified_at.strftime("%Y-%m-%d %H:%M")
        )
        return verified_at


class ProfileSerializer(serializers.ModelSerializer):
    kycObject = serializers.SerializerMethodField()
    addressObject = serializers.SerializerMethodField()
    bankObject = serializers.SerializerMethodField()
    user_email = serializers.SerializerMethodField()
    time_joined = serializers.SerializerMethodField()
    last_login = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        exclude = ("id",)
        read_only_fields = ["user"]

    def get_bankObject(self, instance):
        try:
            userBankQS = UserBankAccount.objects.filter(user=instance)
            if userBankQS.exists():
                userBank = userBankQS.first()
                serializer = BankAccountSerializer(userBank, context=self.context)
                return serializer.data
            else:
                return None
        except Exception as e:
            print("exception error", e)
            return None

    def get_kycObject(self, instance):
        try:
            userKYCQS = UserKYC.objects.filter(user=instance)
            # print(userKYCQS)
            if userKYCQS.exists():
                userKYC = userKYCQS.first()
                serializer = ProfileKYCSerializer(userKYC, context=self.context)
                return serializer.data
            else:
                return None
        except Exception as e:
            print("exception", e)
            return None

    def get_user_email(self, object):
        return object.user.email

    def get_time_joined(self, object):
        created_at = object.created_at
        time_delta = created_at.strftime("%Y-%m-%d %H:%M")
        return time_delta

    def get_last_login(self, object):
        the_last_login = object.last_login
        return the_last_login

    def get_addressObject(self, instance):
        try:
            userAddressQS = Address.objects.filter(user=instance)
            # print(userKYCQS)
            if userAddressQS.exists():
                userAddress = userAddressQS.first()
                serializer = AddressSerializer(userAddress, context=self.context)
                return serializer.data
            else:
                return None
        except Exception as e:
            print("exception", e)
            return None
