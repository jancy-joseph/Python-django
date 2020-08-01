from django.urls import path
from . import views

urlpatterns = [
    path('',views.redirectRoottoShowsFunc),
    path('shows',views.showsAllFunc),
    path('shows/new',views.showAddNewFunc),
    path('shows/<int:my_id>',views.showsByIDfunc),
    path('shows/<int:my_id>/update',views.updateShowDBFunc),
    path('shows/<int:my_id>/edit',views.editShowFunc),
    path('shows/<int:my_id>/destroy',views.deleteShowFunc)
]