# forms.py 
from django import forms
from .models import Image, Comment
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView


class PhotoForm(forms.ModelForm):
    class Meta:
        username = forms.CharField(initial='janek')
        model = Image
        fields = ['description', 'image']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
