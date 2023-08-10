from django.urls import path

from . import views

urlpatterns = [
    path("query/", views.index, name="index"),
]