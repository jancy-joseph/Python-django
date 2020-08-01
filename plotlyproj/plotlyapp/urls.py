from django.urls import path,include
from . import views

urlpatterns = [
    path('chart',views.index),
    path('', views.dashboard_with_pivot, name='dashboard_with_pivot'),
    path('data', views.pivot_data, name='pivot_data'),
]