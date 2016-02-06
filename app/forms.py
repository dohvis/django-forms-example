from django import forms
from .models import Post


class ModelFormExample(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('category', 'tag', 'title', 'content')
