from django.shortcuts import render, HttpResponse,redirect

def indexfunction(request):
    return render (request,"index.html")

def nextpagefunction(request):
    context = {
        "name": request.POST["Name"],
        "location": request.POST["Location"],
        "language": request.POST["Language"],
        "comment":request.POST["Comment"],
    }
    print(request.POST)
    print("hellossdsdsdsa   i am here")
    return render(request, "next_page.html",context)

