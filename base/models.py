from contextlib import nullcontext
from django.db import models
from django.forms import CharField, UUIDField

# Create your models here.

class Room(models.Model):

    roomId=models.UUIDField()
    name=models.CharField(max_length=200)
    description=models.TextField(null=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"< Room id : {str(self.roomId)} | Room name : {str(self.name)} >"
