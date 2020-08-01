from django.shortcuts import render,redirect,HttpResponse
from .models import *

from django.contrib import messages
# Create your views here.

def redirectRoottoShowsFunc(request):
    return redirect("/shows")

def showsByIDfunc(request,my_id):
    context={
        "show":Show.objects.all().get(id =my_id)
    }
    return render(request,"showOneTVShow.html",context)
def showsAllFunc(request):
    context={
        "shows":Show.objects.all()
    }
    return render(request,"allShows.html",context)

def showAddNewFunc(request):
    if request.method == "GET":
        return render(request,"addShow.html")
    if(request.method == "POST"):
        errors = Show.objects.show_validate(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value, extra_tags=key)
        return redirect('/shows/new')
    else:
        s1 = Show.objects.create(Title=request.POST['Title'],Network= request.POST['Network'],Release_Date=request.POST['Release_Date'],desc=request.POST['desc'])
        return redirect("/shows/"+str(s1.id))
# Create your views here.

def editShowFunc(request,my_id):
    if request.method == "GET":
        context={
            "show":Show.objects.get(id = my_id),
        }
        print(context['show'].Release_Date)
        return render(request,"editOneTvShow.html",context)

def updateShowDBFunc(request,my_id):
    if(request.method == "POST"):
        errors = Show.objects.show_validate(request.POST)
        if len(errors) > 1:
            for key, value in errors.items():
                if(key != 'name_taken'):
                    messages.error(request, value, extra_tags=key)
            return redirect('/shows/'+str(my_id)+'/edit')
        elif len(errors) == 1:
            for key, value in errors.items():
                if(key == 'name_taken'):
                    updateObj = Show.objects.get(id = my_id)
                    updateObj.Title=request.POST['Title']
                    updateObj.Network= request.POST['Network']
                    updateObj.Release_Date=request.POST['Release_Date']
                    updateObj.desc=request.POST['desc']
                    updateObj.save()
                    return redirect("/shows/"+str(updateObj.id))
        # else:
        #     updateObj = Show.objects.get(id = my_id)
        #     updateObj.Title=request.POST['Title']
        #     updateObj.Network= request.POST['Network']
        #     updateObj.Release_Date=request.POST['Release_Date']
        #     updateObj.desc=request.POST['desc']
        #     updateObj.save()
        #     return redirect("/shows/"+str(updateObj.id))

def deleteShowFunc(request,my_id):
    if request.method == "GET":
        showselected = Show.objects.all().get(id = my_id)
        showselected.delete()
    return redirect("/shows")
