from django.shortcuts import render,redirect
from time import gmtime, strftime
import datetime
    
def index(request):
    context = {
        "time": strftime("%Y-%m-%d %H:%M %p", gmtime())
    }
    return render(request,'index.html', context)
def mytimefunc(request):
    context = {
        "time": datetime.datetime.now()
    }
    return render(request,'index.html', context)

def getandpostfunc(request):
    if request.method == "GET":
        print("a GET request is being made to this route")
        return render(request, "get_post.html")
    if request.method == "POST":
        val_from_field_one = request.POST["one"]
        val_from_field_two = request.POST["two"]
        print(val_from_field_one)
        print(val_from_field_two)
        print(request.POST)   
        return redirect("/")

