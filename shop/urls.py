from django.urls import path, include
from .views import *
from django.contrib.auth.decorators import login_required

app_name = "shop"

urlpatterns = [
    path("item-list/", login_required(ItemList.as_view()), name="item-list"),
    path("shop-orders/", my_shop_orders, name="shop-orders"),
    path("delete-item/<item_id>/", delete_item, name="delete-item"),
    path(
        "item-details/<item_id>/",
        login_required(ItemDetail.as_view()),
        name="item-details",
    ),
]
