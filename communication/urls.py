# a path for all url redirections within this module
from django.urls import path
from . import views

app_name='communication'

# set the redirections
urlpatterns = [
    path('', views.inbox, name='inbox'),
    path('<int:pk>/', views.detail, name='detail'),
    path('new/<int:item_pk>/', views.new_communication, name='new'),
]
