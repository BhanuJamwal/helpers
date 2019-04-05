from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from Status .models import Boards,Topic,Post
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import NewTopicForm,PostForm,NewBForm
from django.db.models import Count
from django.views.generic import UpdateView, ListView
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
# Create your views here.



class BoardListView(ListView):
    model=Boards
    context_object_name = 'boards'
    template_name = 'Status/home.html'

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
    board = get_object_or_404(Boards, pk=pk)
    queryset = board.topics.order_by('-last_updated').annotate(replies=Count('posts')-1)
    page=request.GET.get('page',1)
    paginator=Paginator(queryset,20)
    try:
        topics = paginator.page(page)
    except PageNotAnInteger:
        # fallback to the first page
        topics = paginator.page(1)
    except EmptyPage:
        # probably the user tried to add a page number
        # in the url, so we fallback to the last page
        topics = paginator.page(paginator.num_pages)
    return render(request, 'Status/topics.html', {'board': board,'topics':topics})

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
    topic.views += 1
    topic.save()
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

@method_decorator(login_required, name='dispatch')
class PostUpdateView(UpdateView):
    model=Post
    fields=('message',)
    template_name='Status/edit_post.html'
    pk_url_kwarg='post_pk'
    context_object_name='post'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(created_by=self.request.user)

    def form_valid(self,form):
        post=form.save(commit=False)
        post.updated_by=self.request.user
        post.updated_at=timezone.now()
        post.save()
        return redirect('topic_posts', pk=post.topic.board.pk, topic_pk=post.topic.pk)