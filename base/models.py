from contextlib import nullcontext
from turtle import mode
from unittest.util import _MAX_LENGTH
from django.db import models
from django.forms import CharField, UUIDField
from django.contrib.auth.models import User

import uuid
# Create your models here.

class Room(models.Model):

    roomId=models.IntegerField(null=False) 
    name=models.CharField(max_length=200)
    topic = models.ForeignKey('Topic',on_delete=models.SET_NULL,null=True)
    description=models.TextField(null=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"< Room id : {str(self.roomId)} | Room name : {str(self.name)} >"

class Message(models.Model):
    user=models.ForeignKey(User,on_delete = models.CASCADE)
    room = models.ForeignKey(Room,on_delete = models.CASCADE)
    body=models.TextField()
    updated=models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Room message preview : {self.body[:50]}"
    
class Topic(models.Model):
    topic =models.CharField(max_length=200)

    def __str__(self):
        return f"Topic : {self.topic}"