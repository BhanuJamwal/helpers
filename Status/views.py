from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from Status .models import Boards,Topic,Post

from django.contrib.auth.models import User
from .forms import NewTopicForm
# Create your views here.



def home(request):
    boards=Boards.objects.all()
    return render(request,'Status/home.html',{"boards":boards})

def board_topics(request, pk):
    board = Boards.objects.get(pk=pk)
    return render(request, 'Status/topics.html', {'board': board})

from django.contrib.auth.models import User
from .forms import NewTopicForm


def new_topic(request, pk):
    board = get_object_or_404(Boards, pk=pk)
    user = User.objects.first()  # TODO: get the currently logged in user
    if request.method == 'POST':
        form = NewTopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.board = board
            topic.starter = user
            topic.save()
            post = Post.objects.create(
                message=form.cleaned_data.get('message'),
                topic=topic,
                created_by=user
            )
            return redirect('board_topics', pk=board.pk)  # TODO: redirect to the created topic page
    else:
        form = NewTopicForm()
    return render(request, 'Status/new_topic.html', {'board': board, 'form': form})