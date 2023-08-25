# importing required libraries
from django.contrib.auth.models import User
from django.db import models
from item.models import Item

# a class to get the item of communication, members involved and the details of the communication itself such as when the message was created/modified
class Communication(models.Model):
    item = models.ForeignKey(Item, related_name='communications', on_delete=models.CASCADE)
    members = models.ManyToManyField(User, related_name='communications')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ('-modified_at',)

# similarly a class for getting the details of each unique message
class ConversationMessage(models.Model):
    communication = models.ForeignKey(Communication, related_name='messages', on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='created_messages', on_delete=models.CASCADE)
    
    