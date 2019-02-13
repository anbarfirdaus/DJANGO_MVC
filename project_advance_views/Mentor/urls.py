from django.urls import path
from . import views

urlpatterns = [
    path('', views.Mentor, name='Mentor'),
    path('db_mentor/', views.db_mentor, name='db_mentor'),
    path('post_new/', views.input_post, name='input_post'),
]