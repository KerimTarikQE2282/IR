
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("ir/", include("irapp.urls")),
    path("admin/", admin.site.urls),
]