from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
# Create your views here.

def pollview(request):
    polls = PollModel.objects.all()
    
    context = {'polls' : polls}
    return render(request,"pollapp/poll.html",context)

def upvote(request,id):
    poll = PollModel.objects.get(id = id)
    poll.upvotes = int(poll.upvotes)+1
    poll.save()
    messages.add_message(request,messages.INFO,"upvote successful")
    return redirect(request.META['HTTP_REFERER'])

def downvote(request,id):
    poll = PollModel.objects.get(id = id)
    poll.downvotes = int(poll.downvotes)+1
    poll.save()
    messages.add_message(request,messages.INFO,"downvote successful")
    return redirect(request.META['HTTP_REFERER'])