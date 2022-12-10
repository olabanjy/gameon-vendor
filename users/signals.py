from django.dispatch import receiver
from django.db.models.signals import pre_save
from django.contrib.auth.signals import (
    user_logged_in,
    user_logged_out,
    user_login_failed,
)
from .tasks import send_login_notification, save_user_login_info
from .models import Profile
from django.contrib.sessions.models import Session
import pyotp

# import ipinfo


@receiver(user_logged_in)
def log_user_login(sender, request, user, **kwargs):
    try:
        save_user_login_info(user.pk)
    except:
        pass


@receiver(user_login_failed)
def log_user_login_failed(sender, credentials, request, **kwargs):
    print("user logged in failed")


@receiver(user_logged_out)
def log_user_logout(sender, request, user, **kwargs):
    print(f"{user}user logged out")


def generate_key():
    """Profile otp key generator"""
    key = pyotp.random_base32()
    if is_unique(key):
        return key
    generate_key()


def is_unique(key):
    try:
        Profile.objects.get(key=key)
    except Profile.DoesNotExist:
        return True
    return False


@receiver(pre_save, sender=Profile)
def create_key(sender, instance, **kwargs):
    """This creates the key for users that don't have keys"""
    if not instance.key:
        instance.key = generate_key()
