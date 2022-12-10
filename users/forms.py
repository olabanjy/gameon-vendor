from django import forms
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget
from .models import *


GENDER = (("Male", "Male"), ("Female", "Female"))

PASSPORT = 0
NATIONAL_ID = 1
DRIVING_LICENSE = 2
DOC_TYPE = (
    (PASSPORT, "Passport"),
    (DRIVING_LICENSE, "Driving License"),
    (NATIONAL_ID, "National ID"),
)


class ProfileSetUpForm(forms.Form):
    first_name = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={"class": "form-control", "first_name": "first_name"}
        ),
    )
    last_name = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={"class": "form-control", "last_name": "last_name"}
        ),
    )
    phone = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "id": "phone",
                "type": "tel",
            }
        ),
    )
    dob = forms.DateField(
        required=True,
        widget=forms.DateInput(
            attrs={
                "class": "form-control",
                "type": "date",
                "placeholder": "mm/dd/yyyy",
                "id": "dob",
            }
        ),
    )
    gender = forms.ChoiceField(
        required=True,
        choices=GENDER,
        widget=forms.Select(
            attrs={"class": "form-control form-select ", "id": "gender"}
        ),
    )
    address_1 = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={"class": "form-control form-control-lg"}),
    )

    account_number = forms.CharField(
        required=True,
        widget=forms.NumberInput(
            attrs={"class": "form-control form-control-lg", "maxlength": "10"}
        ),
    )

    account_name = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={"class": "form-control form-control-lg"}),
    )

    account_bank = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={"class": "form-control form-control-lg"}),
    )

    city = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={"class": "form-control", "id": "city"}),
    )

    state = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={"class": "form-control", "id": "state"}),
    )

    # occupation = forms.CharField(
    #     required=False,
    #     widget=forms.TextInput(attrs={"class": "form-control", "id": "occupation"}),
    # )

    shop_name = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={"class": "form-control", "id": "shop_name"}),
    )

    document_front = forms.FileField(
        required=True,
        widget=forms.FileInput(
            attrs={
                "id": "id_front",
                "accept": "file_extension|.pdf, .jpg, .png, .jpeg",
                "class": "kyc_file",
            }
        ),
    )
    document_back = forms.FileField(
        required=False,
        widget=forms.FileInput(
            attrs={
                "id": "id_back",
                "accept": "file_extension|.pdf, .jpg, .png, .jpeg",
                "class": "kyc_file",
            }
        ),
    )

    doc_type = forms.ChoiceField(choices=DOC_TYPE, widget=forms.RadioSelect())

    t_and_c = forms.BooleanField(
        required=True,
        widget=forms.CheckboxInput(
            attrs={"class": "custom-control-input", "id": "tc-agree"}
        ),
    )

    def clean(self):
        cleaned_data = super().clean()
        phone = cleaned_data.get("phone")
        first_name = cleaned_data.get("first_name")
        document_front = cleaned_data.get("document_front")
        document_back = cleaned_data.get("document_back")
        try:
            if phone:
                user_exists = Profile.objects.filter(phone=phone).first()
                if user_exists and user_exists.first_name != first_name:
                    raise forms.ValidationError(
                        "A vendor with that phone number already exists! "
                    )

            if document_front:
                if not document_front.name.endswith((".pdf", ".png", ".jpg", ".jpeg")):
                    raise forms.ValidationError(
                        "Wrong File format, must be .pdf or .png or .jpg"
                    )
                if document_front.size > 5242880:
                    raise forms.ValidationError(
                        f"File is too large. Size should not be more than 1MB"
                    )

            if document_back:
                if not document_back.name.endswith((".pdf", ".png", ".jpg", ".jpeg")):
                    raise forms.ValidationError(
                        "Wrong File format, must be .pdf or .png or .jpg"
                    )
                if document_back.size > 5242880:
                    raise forms.ValidationError(
                        "File is too large. Size should not be more than 1MB"
                    )

            return cleaned_data

        except (ValueError, NameError, TypeError, ImportError, IndexError) as error:
            err_msg = str(error)
            raise forms.ValidationError(err_msg)
            return cleaned_data
            print(err_msg)


class AccountSettingsForm(forms.Form):
    shop_name = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={"class": "form-control form-control-lg", "id": "shop_name"}
        ),
    )
    address_1 = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={"class": "form-control form-control-lg"}),
    )

    account_number = forms.CharField(
        required=False,
        widget=forms.NumberInput(
            attrs={"class": "form-control", "maxlength": "10", "id": "account_number"}
        ),
    )

    account_name = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={"class": "form-control", "id": "account_name"}),
    )

    account_bank = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={"class": "form-control", "id": "account_bank"}),
    )

    city = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={"class": "form-control", "id": "city"}),
    )

    state = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={"class": "form-control", "id": "state"}),
    )
    phone = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control form-control-lg",
                "id": "phone",
                "type": "tel",
            }
        ),
    )
    photo = forms.FileField(
        required=False,
        widget=forms.FileInput(
            attrs={
                "id": "photo",
                "accept": ".jpg, .png, .jpeg",
                "class": "photo form-control form-control-lg",
            }
        ),
    )

    def clean(self):
        cleaned_data = super().clean()
        photo = cleaned_data.get("photo")
        try:
            if photo:
                if not photo.name.endswith((".png", ".jpg", ".jpeg")):
                    raise forms.ValidationError(
                        "Wrong File format, must be or .png or .jpg"
                    )

            return cleaned_data

        except (ValueError, NameError, TypeError, ImportError, IndexError) as error:
            err_msg = str(error)
            print(err_msg)
            raise forms.ValidationError(err_msg)
