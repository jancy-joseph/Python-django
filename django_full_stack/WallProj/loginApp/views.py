from django.shortcuts import render,redirect,HttpResponse
from .models import *
from django.contrib import messages
import bcrypt

# Create your views here.
def index(request):
    if request.method == "GET":
        return render(request,"login_registration.html")
    elif request.method == "POST":
        if request.POST['myform'] == "1":
            errors = User.objects.registration_validate(request.POST)
            if len(errors) > 0:
                for key, value in errors.items():
                    messages.error(request, value, extra_tags=key)
                return redirect('/')
            else:
                password = request.POST['password']
                pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()  # create the hash    
                print(pw_hash)      # prints something like b'$2b$12$sqjyok5RQccl9S6eFLhEPuaRaJCcH3Esl2RWLm/cimMIEnhnLb7iC'    
                # be sure you set up your database so it can store password hashes this long (60 characters)
                # make sure you put the hashed password in the database, not the one from the form!
                User.objects.create(first_name =request.POST['first_name'], last_name =request.POST['last_name'],email=request.POST['email'],birthday_date=request.POST['birthday_date'],password=pw_hash) 
                return redirect("/") # never render on a post, always redirect! 
        elif request.POST['myform'] == "2":
            errors = User.objects.login_validate(request.POST)
            if len(errors) > 0:
                for key, value in errors.items():
                    print(key,value)
                    messages.error(request, value, extra_tags=key)
                return redirect('/')
            else:
                # # see if the username provided exists in the database
                # user = User.objects.filter(email=request.POST['login_email']) # why are we using filter here instead of get?
                # if user: # note that we take advantage of truthiness here: an empty list will return false
                #     logged_user = user[0] 
                #     # assuming we only have one user with this username, the user would be first in the list we get back
                #     # of course, we should have some logic to prevent duplicates of usernames when we create users
                #     # use bcrypt's check_password_hash method, passing the hash from our database and the password from the form
                #     if bcrypt.checkpw(request.POST['login_password'].encode('utf8'), logged_user.password.encode()):
                #         # if we get True after checking the password, we may put the user id in session
                #         request.session['userid'] = logged_user.id
                #         # never render on a post, always redirect!
                myuser = User.objects.filter(email=request.POST['login_email'])
                print(myuser)
                if myuser: # note that we take advantage of truthiness here: an empty list will return false
                    logged_user = myuser[0] 
                    print(logged_user.id)
                    request.session['username'] =logged_user.first_name
                    return redirect('/wall')
                #if we didn't find anything in the database by searching by username or if the passwords don't match, 
                # redirect back to a safe route
                return redirect("/")
