from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index),
    path('mydate',views.mytimefunc),
    path('getandpost',views.getandpostfunc)
]