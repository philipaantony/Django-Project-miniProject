from django.db import models
from django import forms

class User(models.Model):
    name = models.CharField("Full Name",max_length=25)
    email = models.EmailField("Email", unique=True)
    phone = models.CharField("Phone No", max_length=25)
    pswd = models.CharField("Password", max_length=25)

class Blog(models.Model):
    userid = models.IntegerField(default=0)
    useremail = models.EmailField("Email")
    username = models.CharField(" Name",max_length=25)
    blogtitle = models.CharField("Title",max_length=25)
    blogcontent = models.TextField("Content",max_length=10000)
