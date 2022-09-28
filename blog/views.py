from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404, redirect
from .forms import PostForm, CommentForm, SearchForm
from django.contrib.auth.models import User
from users.models import Profile
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (ListView, DetailView, DeleteView, CreateView, UpdateView)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import PostSerializer
import os
import time
import datetime

path = os.getcwd()

class PostListView(ListView):
    model = Post
    template_name = 'blog/base.html'
    context_object_name = 'posts'
    ordering = ['-published_date']


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'   
 

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title','text']
    template_name = 'blog/post_edit.html'
    login_url = '/login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title','text']
    template_name = 'blog/post_edit.html'
    login_url = '/login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False        


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False 


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment_to_post.html', {'form': form})


def about(request):
    now = str(time.asctime(time.localtime(time.time())))
    return render(request, 'blog/about.html', {'title': now})


def search(request):
    p = Post.objects.all()
    u = User.objects.all()
    pr = Profile.objects.all()
    if request.method =='POST':
        s_form = SearchForm(request.POST)
        search_keyword = request.POST['search']
        print(search_keyword)
    return render(request, 'blog/searchresults.html', {'results': search_keyword})
    