from django.shortcuts import render,HttpResponse,redirect
from .models import User

# Create your views here.
def index(request):
    context={
        "User":User.objects.all()
    }
    return render(request,"index.html",context)

def userAddDisplayFunc(request):
    if request.method == "GET":
        return redirect("/")
    if(request.method == "POST"):
        User.objects.create(first_name=request.POST['first_name'],last_name=request.POST['last_name'],email_address=request.POST['email_address'],age=request.POST['age'])
        return redirect("/")