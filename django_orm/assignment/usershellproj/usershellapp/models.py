from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email_address = models.CharField(max_length=255)
    age=models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return f'<User Object# first_name: {self.first_name} last_name: {self.last_name} EmailAddress: {self.email_address} age: {self.age} created_at:{self.created_at} updated_at{self.updated_at}>'

