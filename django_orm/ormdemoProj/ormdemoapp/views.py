from django.shortcuts import render,HttpResponse
from .models import *
from . import views

# Create your views here.
def index(request):
    context={
        "charatcters":DisneyCharacter.objects.all()
    }
    return render("index.html",context)
