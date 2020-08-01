from django.urls import path
from . import views

urlpatterns = [
    path('postfunc', views.postfunc),
]