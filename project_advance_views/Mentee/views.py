from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Mentee
from .forms import PostForm

# Create your views here.

def Mentee(request):
    return render(request,'Mentee/Mentee.html',{})

def db_mentee(request):
    mentee = Mentee.objects.all()
    return render(request,'Mentee/Mentee.html', {'mentees':mentee})

def input_post(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('Mentee')
    else:
        form = PostForm()
    return render(request,'Mentee/post_new.html', {'forms':form})