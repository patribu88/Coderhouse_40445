from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(("home.urls", "home"))),
    path("producto/", include(("producto.urls", "producto"))),
    path("venta/", include(("venta.urls", "venta"))),
]
