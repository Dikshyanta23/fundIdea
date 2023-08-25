# all the necessary imports
from django.urls import path
from . import views

app_name='item'

# set the redirection paths within the module
urlpatterns = [
    path('', views.items, name='items'),
    path('new/', views.new, name='new'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/edit/', views.edit, name='edit'),
]
