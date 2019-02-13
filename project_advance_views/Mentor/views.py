from django.shortcuts import render, redirect
from .models import Mentor
from .forms import PostForm

# Create your views here.

def Mentor(request):
    return render(request,'Mentor/Mentor.html', { })

def db_mentor(request):
    mentor = Mentor.objects.all()
    return render(request, 'Mentor/Mentor.html', {'mentors': mentor})

def input_post(request):
    if request.method =="POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('Mentor')
    else:
        form = PostForm()
    return render(request, 'Mentor/post_new.html', {'forms': form})