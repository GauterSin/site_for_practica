from django.shortcuts import render
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy
from .models import Post, Comment
from django.contrib.auth.models import User
from .forms import PostForm, CommentForm


def index(request):
    form = PostForm()
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PostForm(request.POST, request.FILES)
            if form.is_valid():
                pos = form.save(commit = True)
                pos.author = request.user
                pos.save()
    list_post = Post.objects.all()
    data = {
        'list_post': list_post,
        'form': form,
    }
    return render(request, 'news.html', data)


def post(request, slug):
    form = CommentForm()
    list_post = Post.objects.get(slug = slug)
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = CommentForm(request.POST, request.FILES)
            if form.is_valid():
                pos = form.save(commit = True)
                pos.author = request.user
                pos.post = list_post
                pos.save()
    
    list_comment = Comment.objects.filter(post = list_post)
    data = {
        'list_post': list_post,
        'form': form,
        'list_comment': list_comment
    }
    return render(request, 'post.html', data)



class Logout(LogoutView):
    next_page = reverse_lazy('index')

    