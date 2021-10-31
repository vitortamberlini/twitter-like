from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'twitter/index.html')


def base(request):
    return render(request, 'twitter/base.html')

