from django.shortcuts import render

# Create your views here.
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
                    request.session['user_id'] = logged_user.id
                    return redirect('/success')
                #if we didn't find anything in the database by searching by username or if the passwords don't match, 
                # redirect back to a safe route
                return redirect("/")

def wallFrontPageFunc(request):
    if 'username' not in request.session:
        return redirect("/")
    context={
        "posts":Post.objects.all()
    }
    return render(request,"success.html",context)

def clearSessionsFunc(request):
    request.session.flush()
    return redirect("/")

def addPostFunc(request):
    if(request.method == "POST"):
        userobj = User.objects.get(first_name =request.session['username'])
        entiremessage = request.POST['Authormessage']+":"+request.POST['Quotemessage']
        Post.objects.create(message=entiremessage,likecount = 0,user=userobj)
        return redirect("/success")

def PostLikeFunc(request,my_post_id):
    if(request.method == "POST"):
        userobj = User.objects.get(first_name =request.session['username'])
        postobj = Post.objects.get(id = my_post_id)
        postobj.likecount = postobj.likecount + 1
        postobj.save()
        Like.objects.create(likeSet=True,user=userobj,post=postobj)
        return redirect("/success")
    else:
        return redirect("/success")

def DeletePostFunc(request,my_post_id):
        postobj = Post.objects.get(id = my_post_id)
        postobj.delete()
        return redirect("/success")

def ViewUserPostsFunc(request,my_post_user_id):
    myuser = User.objects.get(id = my_post_user_id)
    fullname = myuser.first_name+ " "+myuser.last_name
    # mypostfiltered = Post.objects.filter(user =myuser )
    context={
        "userposts":Post.objects.filter(user=myuser),
        "mypostusername":fullname
    }
    return render(request,"mypost.html",context)

def EditMyAccountFunc(request,my_user_id):
    context={
            "mynewuser":User.objects.get(id = my_user_id)
    }
    return render(request,"myedit.html",context)

def UpdateMyAccountFunc(request,my_user_id):
    if request.POST['myform'] == "edit2":
            errors = User.objects.registration_validate(request.POST)
            if len(errors) > 1:
                for key, value in errors.items():
                    if(key != 'email_taken'):
                        messages.error(request, value, extra_tags=key)
                return redirect("/"+str(my_user_id)+"/Update")
            elif len(errors) == 1:
                for key, value in errors.items():
                    if(key == 'email_taken'):
                        updateObj = User.objects.get(id = my_user_id)
                        updateObj.first_name = request.POST['first_name']
                        updateObj.last_name = request.POST['last_name']
                        updateObj.email = request.POST['email']
                        updateObj.save()
                        return redirect("/success") # never render on a post, always redirect! 


