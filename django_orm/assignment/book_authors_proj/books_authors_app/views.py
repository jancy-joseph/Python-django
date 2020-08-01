from django.shortcuts import render,redirect,HttpResponse
from .models import Book,Author

def indexfunc(request):
    context={
        "books":Book.objects.all()
    }
    return render(request,"index.html",context)

    
def addBookFunc(request):
    if request.method == "GET":
        return redirect("/")
    if(request.method == "POST"):
        Book.objects.create(title=request.POST['title'],desc=request.POST['desc'])
        return redirect("/")

def showBookInfoFunc(request,my_val):
    if request.method == "GET":
        Bookselected = Book.objects.all().get(id = my_val)
        context={
            "book":Bookselected,
            "allexcluded_authors": Author.objects.all().exclude(books=Book.objects.all().get(id=my_val)),
        }
        return render(request,"Books.html",context)