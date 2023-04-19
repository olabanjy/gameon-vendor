from django.template.loader import render_to_string
from django.core.mail import send_mail, EmailMessage

from .models import *


def send_rental_item_approved_email(item_id):
    try:
        the_item = RentalGame.objects.get(id=item_id)
        subject, from_email, to = (
            "Rental Item Approved",
            "GameOn <noreply@gameon.com.ng>",
            [the_item.vendor.user.email],
            # ["shola.albert@gmail.com"],
        )

        html_content = render_to_string(
            "events/rental_item_approved.html",
            {
                "item_name": the_item.name,
                "vendor_fullname": f"{the_item.vendor.first_name} {the_item.vendor.last_name}",
            },
        )
        msg = EmailMessage(subject, html_content, from_email, to)
        msg.content_subtype = "html"
        msg.send()
    except Exception as e:
        print(e)
        pass
