from django.db import models

# Create your models here.
class UserPlotData(models.Model):  
    avgLbsPerReps = models.DecimalField(max_digits=5, decimal_places=2)
    week = models.IntegerField()
    date = models.DateField()
    username = models.CharField(max_length=255)
    # confirm_password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __repr__(self):
        return f'\nID: {self.id}\tuser:{self.username} \tWeek :{self.week}\t email: {self.date}\t'
