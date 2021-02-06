from django.shortcuts import render #render used to access Templates
from django.http import HttpResponse #handles traffic from the homepage of our blog

# Create your views here.

def home(request):
    return render(request, 'blog/home.html')

def about(request):
    return render(request, 'blog/about.html')
