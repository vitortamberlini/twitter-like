from django.http import HttpResponse
from django.shortcuts import render
from .models import Post


def index(request):
    return render(request, 'twitter/index.html')


def base(request):
    return render(request, 'twitter/base.html')


def posts(request):
    all_posts = list(Post.objects.all())

    context = {
        'posts': all_posts
    }

    print(all_posts)

    return render(request, 'twitter/posts.html', context=context)
