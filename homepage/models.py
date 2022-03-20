from random import choices
from django.db import models
from django.contrib.auth.models import User

import datetime
YEAR_CHOICES = []
for r in range(1980, (datetime.datetime.now().year+3)):
    YEAR_CHOICES.append((r,r))


class student(models.Model):
    #user= models.ForeignKey(User, null=True , on_delete=models.CASCADE)
    user= models.OneToOneField(User, null=True , on_delete=models.CASCADE)
    cat=(('A','A') , ('B','B'), ('C','C'), ('D','D'), ('E','E'))
    cat2=(('1','1') , ('2','2'))
    name= models.CharField(max_length=100,null=True)
    matric= models.CharField(max_length=100,null=True)
    #semsester=models.CharField(max_length=100, choices=cat2)
    #grade=models.CharField(max_length=100, choices=cat)
    date_created=models.DateTimeField(auto_now_add=True)

    def __str__(self) :
        return self.name

class course(models.Model):
    cat=(('A','A') , ('B','B'), ('C','C'), ('D','D'), ('E','E'))
    cat2=(('1','1') , ('2','2'))
    name=models.CharField(max_length=100,null=True)
    student=models.ManyToManyField(student)
    date_created=models.DateTimeField(auto_now_add=True)
    grade=models.CharField(max_length=100, choices=cat,null=True)
    unit=models.IntegerField(null=True)
    semsester=models.CharField(max_length=100, choices=cat2, null=True)
    #year = models.IntegerField(('year'), max_length=4, choices=YEAR_CHOICES, default=datetime.datetime.now().year, null=True)
    year=models.IntegerField( null=True)
    def __str__(self) :
       return self.name


#class year(models.Model):
#    year = models.IntegerField(('year'), max_length=4, choices=YEAR_CHOICES, default=datetime.datetime.now().year, null=True)
#    course = models.ManyToManyField(course)
#    student = models.ManyToManyField(student)
#    def __str__(self) :
#       return self.year


    
    

