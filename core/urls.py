from django.urls import path
from . import views

urlpatterns = [
    path("", views.default, name="default"),
    path("menu/", views.menu, name='menu'),
    path("payment", views.payment, name='payment'),
    path("complete", views.complete, name='complete'),
]