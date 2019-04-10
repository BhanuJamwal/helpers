from django import forms
from .models import Tweet


class NewBForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['name', 'text']