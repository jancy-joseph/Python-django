from django.db import models
from datetime import datetime
import re
from loginApp.models import *

class PostManager(models.Manager):
    def postvalidate(self, postData):
        errors = {}
        return errors

class Post(models.Model):  
    #user_id = models.IntegerField()
    message = models.TextField()
    likecount = models.IntegerField()
    user = models.ForeignKey(User,related_name="user_posts",on_delete=(models.CASCADE))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = PostManager()
    def __repr__(self):
        return f'\nID: {self.id}\t MSG: {self.message}\t'

class CommentManager(models.Manager):
    def commentvalidate(self, postData):
        errors = {}
        return errors

class Comment(models.Model):  
    #message_id = models.IntegerField()
    #user_id = models.IntegerField()
    likeSet = models.BooleanField()
    user = models.ForeignKey(User,related_name="user_comments",on_delete=(models.CASCADE))
    post = models.ForeignKey(Post,related_name="comments",on_delete=(models.CASCADE))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CommentManager()
    def __repr__(self):
        return f'\nID: {self.id}\t comment: {self.comment}\t'