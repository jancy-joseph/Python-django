#from django.shortcuts import render
from django.shortcuts import render, HttpResponse
def index(request):
    # return HttpResponse("this is the equivalent of @app.route('/')!")
    return render(request,"index.html")
def myfunction(request):
    #return HttpResponse("This is my fucntion getting invoked")
    return render(request,"test.html")


# Create your views here.
