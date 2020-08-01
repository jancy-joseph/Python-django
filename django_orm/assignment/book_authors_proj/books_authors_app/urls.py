from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.indexfunc),
    path('addBook',views.addBookFunc),
    path('books/<int:my_val>',views.showBookInfoFunc)
]
