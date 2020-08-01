from django.urls import path,include
from . import views


urlpatterns = [
    path('',views.index),
    path('success',views.successFunc),
    path('logout',views.clearSessionsFunc)
]
