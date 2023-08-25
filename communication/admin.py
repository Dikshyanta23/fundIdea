# import required libraries from django
from django.contrib import admin
from .models import Communication, ConversationMessage

# register the services
admin.site.register(Communication)
admin.site.register(ConversationMessage)


