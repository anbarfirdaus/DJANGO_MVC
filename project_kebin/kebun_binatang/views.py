from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Hewan
from .forms import PostForm


# Create your views here.

def daftar_binatang(request):
    return render(request, 'kebun_binatang/daftar_binatang.html',{})

def db_binatang(request):
    binatang = Hewan.objects.all()
    return render(request,'kebun_binatang/db_binatang.html', {'animals':binatang})

def input_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('db_binatang')
    else:
        form = PostForm()
    return render(request,'kebun_binatang/post_new.html', {'forms':form})