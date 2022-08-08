from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter


from users.api.views import ProfileViewSet
from shop.api.views import ItemsViewSet

from rental.api.views import ItemsViewSet as RentalItemViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()


router.register("vendors", ProfileViewSet)
router.register("shop/items", ItemsViewSet)
router.register("rental/items", RentalItemViewSet)


app_name = "api"
urlpatterns = router.urls
