from django.shortcuts import render, get_object_or_404 #render used to access Templates
from django.http import HttpResponse #handles traffic from the homepage of our blog
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView)


def home(request):
    context = { 'posts': Post.objects.all()}
    return render(request, 'blog/home.html',context)

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html' #<app>/<model>_<viewpoint>.html
    context_object_name = 'posts'
    ordering = ['date']#changes order of post ('-date' of u want blogs in reverse order)
    paginate_by = 5



class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html' #<app>/<model>_<viewpoint>.html
    context_object_name = 'posts'
    #ordering = ['date']#changes order of post ('-date' of u want blogs in reverse order)
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username = self.kwargs.get('username'))
        return Post.objects.filter(author = user).order_by('date')

class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title' , 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user  #saves the new post and sets the author of the logged in post to the author of the new post
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title' , 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user  #saves the new post and sets the author of the logged in post to the author of the new post
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user== post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'
    def test_func(self):
        post = self.get_object()
        if self.request.user== post.author:
            return True
        return False


def about(request):
    return render(request, 'blog/about.html',{'title': 'About'})
