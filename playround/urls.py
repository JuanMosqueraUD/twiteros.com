from django.urls import path
from . import views

urlpatterns = [
    path('datos/' , views.datos)
]