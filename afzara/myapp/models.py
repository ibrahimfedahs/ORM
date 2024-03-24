from django.db import models
from django.contrib import admin
class Football (models.Model):
    name=models.CharField(max_length=100,help_text="FOOTBALL PLAYER")
    jerseyno=models.IntegerField()
    country=models.CharField(max_length=100)
    age=models.IntegerField()
    place=models.IntegerField()

class FootballAdmin(admin.ModelAdmin):
    list_display=('name','jerseyno','country','age','place')
