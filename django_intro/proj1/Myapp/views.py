from django.shortcuts import render, HttpResponse,redirect
def index(request):
    return HttpResponse("placeholder to later display a list of all blogs")
def new(request):
    return HttpResponse("placeholder to display a new form to create a new blog")
def create(request):
    return redirect("/") 
def show(request,my_val):
    return HttpResponse("placeholder to display blog number:"+str(my_val))
def edit(request,my_val):
    return HttpResponse("placeholder to display blog :"+str(my_val))
def destroy(request,my_val):
    return redirect("/") 
def dummy(request,my_id):
    pass
def renderfunc1(request):
    context = {
        "name": "Noelle",
        "favorite_color": "turquoise",
        "pets": ["Bruce", "Fitz", "Georgie"]
    }
    return render(request,"index.html",context)
def imagefunc(request):
    context={
        "myimage":"down1.png"
    }
    return render(request,"static_test.html",context)