from django.urls import path     
from . import views
urlpatterns = [
    #these are the C of CRUD
    path('new', views.new),
    path('create', views.create),
    #these are the R of CRUD
    path('', views.index),
    path('<int:my_val>',views.show),
    #these are the U of CRUD
    path('<int:my_val>/edit',views.edit),
    #these are the U of CRUD
    path('<int:my_val>/delete',views.destroy),	 
    path('/delete/<id>',views.dummy),
    path('renderhtml',views.renderfunc1),
    path('imgcheck',views.imagefunc),
]