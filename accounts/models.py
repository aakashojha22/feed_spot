from django.db import models


from django.contrib.auth.models import User
from django.shortcuts import redirect


# Create your models here.
class UserDetail(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=20,unique=False,null=True)
    budget = models.PositiveIntegerField(blank=True,null=True)
    mobile_no = models.BigIntegerField(blank=True,null=True)
    plot_size = models.PositiveIntegerField(blank=True,null=True)
    address = models.CharField(max_length=150,unique=False,null=True)
    bedrooms = models.PositiveSmallIntegerField(blank=True,null=True)
    bathrooms = models.PositiveSmallIntegerField(blank=True,null=True)
    floors = models.PositiveSmallIntegerField(blank=True,null=True)
    description = models.TextField(blank=True,unique=False,null=True)

    def get_absolute_url(self):
        return redirect("index")

    def __str__(self):
        return  self.user.username

