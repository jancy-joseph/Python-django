from django.urls import path     
from . import views
urlpatterns = [
    path('',views.indexfunction),
    path('result',views.nextpagefunction)
]