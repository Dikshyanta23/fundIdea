# importing necessary modules and libraries
from django.shortcuts import render, redirect
from item.models import Category, Item
from .forms import SignUpForm

# a function to get the index page with all items
def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()
    return render(request, 'core/index.html', {
        'categories': categories,
        'items': items,
    })

# module for contacting the idea source
def contact(request):
    return render(request, 'core/contact.html')

# for about page
def about(request):
    return render(request, 'core/about.html')

# a function for signing up to the application
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        
        if form.is_valid():
            form.save()
            
            return redirect('/login/')
    else:
        form = SignUpForm()
    
    return render(request, 'core/signup.html', {
        'form': form
    })