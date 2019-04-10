from django.shortcuts import render,redirect,HttpResponse,HttpResponseRedirect
from tweet .models import Tweet
from .forms import NewBForm
from django.contrib.auth.models import User
import json
from django.views.generic import View




# Create your views here.
def tweets(request):
	tweets = Tweet.objects.all()
	return render(request, 'tweet/post.html', {'tweets':tweets })

def new_tweet(request):
    user = User.objects.first()
    form=NewBForm(request.POST or None)
    if request.method == 'POST':

        if form.is_valid():
            tweet=form.save(commit=False)
            tweet.user=request.user
            tweet.save()
            return redirect('/tweet/tweets')
        else:
            form=NewBForm()
    return render(request,'tweet/new_tweet.html',{'form':form})

class UserRedirect(View):
  def get(self, request):
  	return HttpResponseRedirect('/user/'+request.user.username)

def follow(request,tweet_id):
    user = request.user
    event = Tweet.objects.get(id=tweet_id)

    event.users.add(user)
    event.save()
