from django.shortcuts import render,redirect,HttpResponse
import datetime
import random


def index(request):
    request.session["points"]= 1
    request.session["mytext"] ="hello"
    return render(request,"index.html")

def processmoneyfunc(request):
    # if request.method == "GET":
    #     print("a GET request is being made to this route")
    #     return redirect("/")
    if request.method == "POST":
        print("hi")
        print(request.POST['Building'])
        # date = str(datetime.datetime.now())
        # if request.POST["Building"]== "1":
        #     my_points = random.randint(10,20)
        #     activity_text="Earned"+str(my_points)+"from the Farm!("+date+")\n"
        # elif request.POST["Building"]== "2":
        #     my_points = random.randint(5,10)
        #     activity_text="Earned"+str(my_points)+"golds from the Cave!("+date+")\n"
        # elif request.session.building_type == "3":
        #     my_points = random.randint(2,5)
        #     activity_text="Earned"+str(my_points)+"golds from the House!("+date+")\n"
        # request.session["points"] += my_points
        # if request.session.building_type =="4":
        #     request.session["choice"] = random.randint(0,1)
        #     if request.session["choice"] == 1:
        #         my_points = random.randint(0,50)
        #         request.session["points"] += my_points
        #         activity_text="Lucky Winner!! Earned"+str(my_points)+"golds from the Casino!("+date+")\n"
        #     elif request.session["choice"] == 0:
        #         my_points = random.randint(0,50)
        #         request.session["points"] -= my_points
        #         activity_text="Entered a casino and lost "+str(my_points)+"golds from the Casino!....ouch..("+date+")\n"
        # request.session["mytext"]+=activity_text
        return render(request,"index.html")
