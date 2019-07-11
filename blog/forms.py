from django import forms
from . import models
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
         model = Post
         fields = ('title', 'text', 'thumb', 'category')

