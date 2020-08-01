from django.db import models

# Create your models here.
# create class first letter capitalized
#django will automatically create that id attribute
#use dbbrowser  for sqllite to see what is in the database
#on command line python manange.py makemaigrations converts our models to db and db.sqlllite3 will show up

class DisneyCharacter(models.Model):
    name = models.CharField(max_length=30)# length is only 30
    description = models.TextField()# length of the textfield is infinite but it is error prone as people can misuse and messa our datatbase
    age= models.IntegerField()
    height = models.DecimalField(max_digits=4,decimal_places=2)
    isPrincess=models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

        return f"<Disney character object: id: {self.id} name: {self.name} description:{self.description} height:{self.height} isPrincess:{self.isPrincess} Create time: {self.created_at} last Updated: {self.updated_at}'>"
    #return "title :    def __repr__(self):
()".format(self.name)
    #return f'id: {self.id} name: {self.name} description:{self.description} height:{self.height} isPrincess:{self.isPrincess} Create time: {self.created_at} last Updated: {self.updated_at}'




