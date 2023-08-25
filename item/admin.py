# imports
from django.contrib import admin
from .models import Category, Item

# register the module specifics to the main app
admin.site.register(Category)
admin.site.register(Item)
