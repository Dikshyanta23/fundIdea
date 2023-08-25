# import necessary libraries
from django.urls import path
from . import views

app_name = 'dashboard'

# set the redirection paths within the section
urlpatterns = [
    path('', views.index, name='index') 
]
