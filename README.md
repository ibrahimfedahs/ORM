# Ex02 Django ORM Web Application
## Date: 06/03/2024

## AIM
To develop a Django application to store and retrieve data from a Book database using Object Relational Mapping(ORM).

## Entity Relationship Diagram

![image](https://github.com/ibrahimfedahs/ORM/assets/150319493/a667fe03-61fe-4c39-81e7-abad5693d077)


## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM
```
File: Models.py

from django.db import models
from django.contrib import admin

class Employee (models.Model):
    Book_DB=models.CharField(max_length=20,primary_key=True)
    SNO=models.CharField(max_length=100)
    NAME=models.IntegerField()
    AUTHOR=models.EmailField()
    PRICE=models.CharField(max_length=100)

class EmployeeAdmin(admin.ModelAdmin):
    list_display=('unique_number','name','age','email','job')

File: Admin.py

from django.contrib import admin
from .models import Employee,EmployeeAdmin

admin.site.register(Employee,EmployeeAdmin)
```
## OUTPUT
![Untitleddd](https://github.com/ibrahimfedahs/ORM/assets/150319493/0835e036-6e6a-45fd-8ee5-0c73ddbc366e)




## RESULT
Thus the program for creating a database using ORM hass been executed successfully
