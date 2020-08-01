from django.shortcuts import render,redirect,HttpResponse
from .models import *
from django.contrib import messages
from django.utils import timezone

from loginApp.models import *

# Create your views here.
def wallFrontPageFunc(request):
    if 'username' not in request.session:
        return redirect("/")
    context={
        "posts":Post.objects.all()
    }
    return render(request,"wall.html",context)

def clearSessionsFunc(request):
    request.session.flush()
    return redirect("/")

def addPostFunc(request):
    if(request.method == "POST"):
        userobj = User.objects.get(first_name =request.session['username'])
        Post.objects.create(message=request.POST['message'],user=userobj)
        return redirect("/wall")

def addCommentToPostFunc(request,my_post_id):
    if(request.method == "POST"):
        userobj = User.objects.get(first_name =request.session['username'])
        postobj = Post.objects.get(id = my_post_id)
        Comment.objects.create(comment=request.POST['comment'],user=userobj,post=postobj)
        return redirect("/wall")

def days_hours_minutes(td):
    #return td.days, td.seconds//3600, (td.seconds//60)%60
    return td.seconds//3600

def deleteCommentToPostFunc(request,my_comment_id):
    uservisitingobj = User.objects.get(first_name =request.session['username'])
    commentobj = Comment.objects.get(id =my_comment_id)
    if(commentobj.user.id == uservisitingobj.id):
        commentobj.delete()
        return redirect("/wall")
    else:
        # messages.error(request, "Dont try deleting others comments ", extra_tags=str(my_comment_id))
        print("Dont try deleting others comments ")
        return redirect("/wall")

def deletePostFunc(request,my_post_id):
    uservisitingobj = User.objects.get(first_name =request.session['username'])
    postobj = Post.objects.get(id = my_post_id)
    if(postobj.user.id == uservisitingobj.id):
        diff = timezone.now() - postobj.created_at
        diffminutes = diff.seconds//60
        print(diffminutes)
        if(diffminutes <30):
            postobj.delete()
        else:
            # messages.error(request, "Not deleteing an older post", extra_tags=str(my_post_id))
            print("Not deleteing an older post")
        return redirect("/wall")
    else:
        # messages.error(request, "Dont try deleting others posts", extra_tags=str(my_post_id))
        print("Dont try deleting others posts")
        return redirect("/wall")





