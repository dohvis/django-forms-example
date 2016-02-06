from django.shortcuts import render


def index(req):
    return render(req, template_name='index.html')
