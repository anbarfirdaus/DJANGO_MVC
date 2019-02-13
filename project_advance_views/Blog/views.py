from django.shortcuts import render,redirect
from .forms import PostForm
from .models import Blog
from .forms import PostForm

# Create your views here.

def Blog(request):
    return render(request,'Blog/Blog.html',{})

def db_blog(request):
    blog = Blog.objects.all()
    return render(request, 'Blog/Blog.html', {'blogs':blog})

def input_post(request):
    if request.method =="POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('Blog')
    else:
        form=PostForm()
    return render(request, 'Blog/new_post_blog.html', {'forms': form})
