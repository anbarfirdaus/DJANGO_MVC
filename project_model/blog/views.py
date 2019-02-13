from django.shortcuts import render,redirect
from django.utils import timezone
from .models import Blog

# from .forms import PostForm
# Create your views here.

def Blog(request):
    return render(request, 'Blog/Blog.html',{})


