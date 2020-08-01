from django.db import models
from datetime import datetime

class ShowManager(models.Manager):
    def show_validate(self, postData):
        errors = {}
        print('I am here')
        allExistingTitles = Show.objects.filter(Title=postData['Title'])
        if len(allExistingTitles) > 0:
            errors['name_taken'] = "Title with that name already exists."
        elif len(postData['Title'])<2:
            errors['Title']="Title should be at least 2 Characters in length."
        if len(postData['Network']) <3:
            errors['Network']="Network should be at least 3 characters in length."
        if len(postData['desc']) >0:
            if len(postData['desc'])<10:
                errors['desc'] ="Description should be at least 3 characters in length"
        try:
            # Validation for making sure discovered date is in the past
            if datetime.strptime(postData['Release_Date'], "%Y-%m-%d") > datetime.now():
                errors['Release_Date'] = "Release Date should be in the past"
        except:
            errors['Release_Date'] = "Stop it you." 
        return errors

# Create your models here.
class Show(models.Model):  
    Title = models.CharField(max_length=255)
    Network = models.CharField(max_length=255)
    Release_Date = models.DateField()
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()
    def __repr__(self):
        return f'\nID: {self.id}\t Title: {self.Title}\t Network: {self.Network}\t Release_Date: {self.Release_Date}\t'

    
# from django.db import models

# # Iport datetime object functionalities
# from datetime import datetime

# # Create your models here.
# class VirusManager(models.Manager):
#     def virus_validate(self, postData):
#         errors = {}

        
#         # Validation for minimum 3 characters in length
#                         # v This is whatever the field in the html is named
#         if len(postData['name']) < 3:
#             errors['name_length'] = "Virus name must be at least 3 characters in length." #<-- This message is going to show up for the user on an invalid submission
#         # Validation for making the name be fewer than 101 characters in length
#         elif len(postData['name']) > 100:
#             errors['name_length'] = "Virus name cannot exceed 100 characters in lenght."
        
#         # Validation for uniqueness
#         viruses = Viruses.objects.filter(name=postData['name'])
#         if len(viruses) > 0:
#             errors['name_taken'] = "Virus with that name already exists."

#         # Checking to make sure that the incubation submitted isn't blank    
#         if len(postData['incubation']) < 1:
#             errors['incubation_time'] = "You must enter an incubation period."
#         # Validation for an actual numerical incubation period longer than 0 days
#         elif int(postData['incubation']) < 1:
#             errors['incubation_time'] = "Virus must incubate for minimum 1 day."
        

#         # WARNING, BE VERY CAREFUL WHEN USING TRY EXCEPTS
#         try:
#             # Validation for making sure discovered date is in the past
#             if datetime.strptime(postData['discovered'], "%Y-%m-%d") > datetime.now():
#                 errors['discovered'] = "Stop messing with the spacetime continuum."
#         except:
#             errors['discovered'] = "Stop it you."    
#         return errors


# class Viruses(models.Model):
#     name = models.CharField(max_length=100)
#     incubation_period = models.IntegerField()
#     discovered = models.DateField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     objects = VirusManager()

