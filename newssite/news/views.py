from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import *


def index(request):
    post = News.objects.all()
    tags = Tags.objects.all()
    return render(request, 'news/home_list.html', {'title':'Главная страница', 'post':post, 'tags':tags, 'tag_selected':0})

def about(request):
    return render(request,'news/about.html', {'title':'О стайте',})


def show_post(request, post_id):
    post = get_object_or_404(News, pk=post_id)
    return render(request, 'news/post.html', {'post':post, 'title':post.title, 'tag_selected':post.tag_id})

def show_tags(request, tag_id):
    post = News.objects.filter(tag_id=tag_id)
    tags = Tags.objects.all()
    return render(request, 'news/home_list.html', {'title': 'Главная страница', 'post': post,'tags': tags, 'tag_selected': tag_id})

