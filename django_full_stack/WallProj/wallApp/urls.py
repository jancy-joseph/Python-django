from django.urls import path,include
from . import views


urlpatterns = [
    path('',views.wallFrontPageFunc),
    path('/logout',views.clearSessionsFunc),
    path('/addpost',views.addPostFunc),
    path('/<int:my_post_id>/addcomment',views.addCommentToPostFunc),
    path('/<int:my_comment_id>/deletecomment',views.deleteCommentToPostFunc),
    path('/<int:my_post_id>/deletepost',views.deletePostFunc)
]
