from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("rental/", include("rental.urls", namespace="rental")),
    path("shop/", include("shop.urls", namespace="shop")),
    path("", include("core.urls", namespace="core")),
    path("finance/", include("finance.urls", namespace="finance")),
    path("u/", include("users.urls", namespace="users")),
    path("accounts/", include("allauth.urls")),
]


urlpatterns += [
    path("api/v1/", include("vendor.api_router")),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [path("__debug__/", include(debug_toolbar.urls))]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
