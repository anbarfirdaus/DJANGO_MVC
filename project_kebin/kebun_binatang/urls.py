from django.urls import path
from . import views

urlpatterns = [
    path('', views.daftar_binatang, name='daftar_binatang'),
    path('db_binatang/', views.db_binatang, name='db_binatang'),
    path('post_new/', views.input_post, name='input_post'),
]