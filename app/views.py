from django.shortcuts import render
from .forms import ModelFormExample


def index(req):
    form = ModelFormExample()
    return render(req, 'index.html', {'form': form})
