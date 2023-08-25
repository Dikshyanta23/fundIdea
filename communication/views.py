# importing the necessary libraries
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from item.models import Item
from .forms import ConversationMessageForm
from .models import Communication

# a function for setting up a new communication between two users
@login_required
def new_communication(request, item_pk):
    item = get_object_or_404(Item, pk=item_pk)
    
    if item.created_by == request.user:
        return redirect('dashboard:index')
    
    communications = Communication.objects.filter(item=item).filter(members__in=[request.user.id])
    
    if communications:
        return redirect('communication:detail', pk=communications.first().id)
    
    if request.method == 'POST':
        form = ConversationMessageForm(request.POST)
        
        if form.is_valid():
            communication = Communication.objects.create(item=item)
            communication.members.add(request.user)
            communication.members.add(item.created_by)
            communication.save()
            
            communication_message = form.save(commit=False)
            communication_message.communication = communication
            communication_message.created_by = request.user
            communication_message.save()
            
            return redirect('item:detail', pk=item_pk)
    else:
        form = ConversationMessageForm() 
        
    return render(request, 'communication/new.html', {
        'form': form,
    })
    
# a function to set up an inbox for each user containing all the interactions with other users    
@login_required
def inbox(request):
    communications = Communication.objects.filter(members__in=[request.user.id])
    
    return render(request, 'communication/inbox.html', {
        'communications': communications,
    })
    
# a function that details each individual communication
@login_required
def detail(request, pk):
    communication = Communication.objects.filter(members__in=[request.user.id]).get(pk=pk)
    
    if request.method == 'POST':
        form = ConversationMessageForm(request.POST)
        
        if form.is_valid():
            communication_message = form.save(commit=False)
            communication_message.communication = communication
            communication_message.created_by = request.user
            communication_message.save()
            
            communication.save()
            
            return redirect('communication:detail',  pk=pk)
        
    else:
        form = ConversationMessageForm()
        
    return render(request, 'communication/detail.html', {
        'communication': communication,
        'form': form,
    })
            
            