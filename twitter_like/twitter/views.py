import json

from django.core.paginator import Paginator, InvalidPage, PageNotAnInteger, EmptyPage
from django.http import HttpResponse, Http404, JsonResponse, HttpResponseBadRequest
from django.shortcuts import render
from django.views.decorators.http import require_GET

from .models import Post


def index(request):
    return render(request, 'twitter/index.html')


def base(request):
    return render(request, 'twitter/base.html')


@require_GET
def feed(request):
    post_list = Post.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(post_list, 10)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, 'twitter/feed.html', {'posts': posts})

