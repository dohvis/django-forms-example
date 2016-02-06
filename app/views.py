from django.shortcuts import (
    render,
    redirect,
)
from django.http import HttpResponse
from .forms import ModelFormExample
from .models import Tag


def index(req):
    if req.method == "POST":
        form = ModelFormExample(req.POST, req)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = req.user
            post.save()
            for tag_pk in req.POST.getlist('tag'):
                post.tag.add(Tag.objects.get(pk=tag_pk))
            post.save()
            return HttpResponse("Post is added successful")
    form = ModelFormExample()
    return render(req, 'index.html', {'form': form})
