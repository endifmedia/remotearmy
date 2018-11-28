
from django.shortcuts import render
from .models import Post


def index(request):
    post_list = Post.objects.all().exclude()
    return render(request, 'blog.html', {'post_list': post_list})


def blogpost(request, post_id):
    bp = Post.objects.get(pk=post_id)
    return render(request, 'single-blog.html', {'blog_post': bp})