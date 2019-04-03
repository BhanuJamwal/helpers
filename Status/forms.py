from django import forms
from .models import Topic,Post,Boards

class NewTopicForm(forms.ModelForm):
    message = forms.CharField(widget=forms.Textarea(), max_length=4000)

    class Meta:
        model = Topic
        fields = ['subject', 'message']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['message', ]

class NewBForm(forms.ModelForm):
    class Meta:
        model = Boards
        fields = ['name', 'description']