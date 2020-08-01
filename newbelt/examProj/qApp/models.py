from django.db import models
from datetime import datetime
import re
import bcrypt

class UserManager(models.Manager):
    def registration_validate(self, postData):
        errors = {}
        print('I am in registration')
        
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        LETTERS_REGEX = re.compile(r'^[A-Za-z0-9_-]*$')

        
        if len(postData['first_name'])<2 and not LETTERS_REGEX.match(postData['first_name']):
            errors['first_name'] = "First Name - at least 2 characters and letters only."
        elif len(postData['first_name'])<2:
            errors['first_name'] = "First Name - at least 2 characters."
        elif not LETTERS_REGEX.match(postData['first_name']):
            errors['first_name'] = "First Name - letters only."
        
        if len(postData['last_name'])<2 and not LETTERS_REGEX.match(postData['last_name']):
            errors['last_name'] = "First Name - at least 2 characters and letters only."
        elif len(postData['last_name'])<2:
            errors['last_name'] = "Last Name - at least 2 characters."
        elif not LETTERS_REGEX.match(postData['last_name']):
            errors['last_name'] = "Last Name - letters only."

        if 'password' in postData:
            if len(postData['password'])<8:
                errors['password'] = "Password - required; at least 8 characters."
            if postData['password']!= postData['confirm_password']:
                errors['match_password'] = "Password do not match."
        
        allExistingEmails = User.objects.filter(email=postData['email'])
        if len(allExistingEmails) > 0:
            errors['email_taken'] = "Email id already esists."
        if not EMAIL_REGEX.match(postData['email']):    # test whether a field matches the pattern            
            errors['email'] = "Invalid email address!"
        
        if 'birthday_date' in postData:
            try:
                #Validation for making sure discovered date is in the past
                if datetime.strptime(postData['birthday_date'], "%Y-%m-%d") > datetime.now():
                    errors['birtday_date'] = "birthday date should be earlier than current date."
            except:
                errors['birtday_date_try_error'] = "Stop it you." 

            try:
                #Validation for making sure age is appropriate
                datediff= (datetime.now() - datetime.strptime(postData['birthday_date'], "%Y-%m-%d"))
                age_limit = datediff.days/365
                if age_limit  < 13:
                    errors['age_limit']= "Must be at least 13 years old."
            except:
                errors['age_limit-tryerrror']= "Age_try_error"
        return errors

    def login_validate(self, postData):
        errors = {}
        print('I am in login validate')
        # allExistingEmails = Show.objects.filter(email=postData['login_email'])
        # if not EMAIL_REGEX.match(postData['login_email']) or len(allExistingEmails)!=1:    # test whether a field matches the pattern            
        #     errors['login_email'] = "Invalid email address!"
        # see if the username provided exists in the database
        user = User.objects.filter(email=postData['login_email']) # why are we using filter here instead of get?
        if user: # note that we take advantage of truthiness here: an empty list will return false
            logged_user = user[0] 
            # assuming we only have one user with this username, the user would be first in the list we get back
            # of course, we should have some logic to prevent duplicates of usernames when we create users
            # use bcrypt's check_password_hash method, passing the hash from our database and the password from the form
            if bcrypt.checkpw(postData['login_password'].encode(), logged_user.password.encode()):
                # if we get True after checking the password, we may put the user id in session
                
                # request.session['userid'] = logged_user.id
                print("passwords match and user found")
                # never render on a post, always redirect!
            else:
                errors['invalid_password']= "Passwords do not match."
        else:
                errors['invalid_email_address'] ="Invalid email address.Please try again."
        return errors


# Create your models here.
class User(models.Model):  
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    birthday_date = models.DateField()
    password =models.CharField(max_length=255)
    # confirm_password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
    def __repr__(self):
        return f'\nID: {self.id}\t Name: {self.first_name}{self.last_name}\t email: {self.email}\t'


class PostManager(models.Manager):
    def postvalidate(self, postData):
        errors = {}
        if len(postData['Authormessage'])<3:
            errors['Authormessage'] = "Author name- at least 2 characters."
        if len(postData['Quotemessage'])<10:
            errors['Authormessage'] = "Author Quote must be at least 10 characters."
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

class Like(models.Model):  
    user = models.ForeignKey(User,related_name="user_likes",on_delete=(models.CASCADE))
    post = models.ForeignKey(Post, related_name="likes",on_delete=(models.CASCADE))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CommentManager()
    def __repr__(self):
        return f'\nID: {self.id}\t'