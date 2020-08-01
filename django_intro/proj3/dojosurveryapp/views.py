from django.shortcuts import render,HttpResponse,redirect

# Create your views here.
def check(request):
    return HttpResponse("hello")

def postfunc(request):
    if request.method == "POST":   
        context = {
            "name1": request.POST["Name"],
            "location1": request.POST["location"],
            "language1": request.POST["language"],
            "comment1":request.POST["Comment"],
        }
        return render(request, "result/next_page.html",context)

