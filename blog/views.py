from django.shortcuts import render #render used to access Templates
from django.http import HttpResponse #handles traffic from the homepage of our blog
from .models import Post





def home(request):
    context = { 'posts': Post.objects.all()}
    return render(request, 'blog/home.html',context)

def about(request):
    return render(request, 'blog/about.html',{'title': 'About'})
