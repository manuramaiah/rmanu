# import necessary libraries
from django.db import models
# from django import forms
# from .models import UserProfile, District, Branch, AccountType, Material
# Create your models here.
# for new user
class Register_User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

    def __str__(self):
        return self.username
# district choice








# creating model for fill the form



class Fill_Form(models.Model):
    user_name=models.CharField(max_length=100)
    date_of_birth=models.DateField(auto_now=False, auto_now_add=False)
    age=models.IntegerField()
    gender=models.CharField(max_length=100)
    phone_number=models.PositiveIntegerField()
    mail_id=models.EmailField()
    address=models.TextField(max_length=200)
    district=models.CharField(max_length=100)
    branch=models.CharField(max_length=100)
    type_of_account=models.CharField(max_length=100)
    materials_provided=models.CharField(max_length=100)

    def __str__(self):
        return self.user_name