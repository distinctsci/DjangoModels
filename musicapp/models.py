from datetime import date
from django.db import models

# Create your models here.
class Artiste(models.Model):
    first_name = models.CharField("first name", max_length = 18)
    last_name = models.CharField("last name", max_length = 18)
    age = models.IntegerField(default = 18)
    
    def __str__(self):
        return self.first_name + " " + self.last_name
    
    
class Song(models.Model):
    id = models.AutoField(default = 0, primary_key = True)
    title = models.CharField(max_length = 18)
    date_released = models.DateField("date released", default=date.today)
    likes = models.IntegerField(default=0)
    artiste = models.ForeignKey(Artiste, default = "", on_delete=models.CASCADE)
   
    def __str__(self):
        return self.title
    
    
class Lyric(models.Model):
    id = models.AutoField(primary_key = True)
    content = models.TextField()
    song = models.ForeignKey(Song, default = "", on_delete=models.CASCADE)
    
    
