from django.http import HttpResponse
from django.shortcuts import render
from .models import Post


def index(request):
    return render(request, 'twitter/index.html')


def base(request):
    return render(request, 'twitter/base.html')


def posts(request):
    all_posts = Post.objects.all()
    return render(request, 'twitter/posts.html')