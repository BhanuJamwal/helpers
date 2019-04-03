from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from Status .models import Boards,Topic,Post
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import NewTopicForm,PostForm,NewBForm
# Create your views here.



def home(request):
    boards=Boards.objects.all()
    return render(request,'Status/home.html',{"boards":boards})

def new_board(request):
    user = User.objects.first()
    form=NewBForm(request.POST or None)
    if request.method == 'POST':

        if form.is_valid():
            board=form.save(commit=False)
            board.starter=request.user
            board.save()
            return redirect('home')
        else:
            form=NewBForm()
    return render(request,'Status/new_board.html',{'form':form})

def board_topics(request, pk):
    board = Boards.objects.get(pk=pk)
    return render(request, 'Status/topics.html', {'board': board})

@login_required
def new_topic(request, pk):
    board = get_object_or_404(Boards, pk=pk)
    user = User.objects.first()  # TODO: get the currently logged in user
    if request.method == 'POST':
        form = NewTopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.board = board
            topic.starter = request.user
            topic.save()
            post = Post.objects.create(
                message=form.cleaned_data.get('message'),
                topic=topic,
                created_by=request.user
            )
            return redirect('topic_posts', pk=pk,topic_pk=topic.pk)  # TODO: redirect to the created topic page
    else:
        form = NewTopicForm()
    return render(request, 'Status/new_topic.html', {'board': board, 'form': form})

def topic_posts(request,pk,topic_pk):
    topic=get_object_or_404(Topic,board__pk=pk,pk=topic_pk)
    return render(request,'Status/topic_posts.html',{'topic':topic})

@login_required
def reply_topic(request, pk, topic_pk):
    topic = get_object_or_404(Topic, board__pk=pk, pk=topic_pk)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.topic = topic
            post.created_by = request.user
            post.save()
            return redirect('topic_posts', pk=pk, topic_pk=topic_pk)
    else:
        form = PostForm()
    return render(request, 'Status/reply_topics.html', {'topic': topic, 'form': form})
