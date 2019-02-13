from django.urls import path
from . import views

urlpatterns = [
    path('', views.Mentee, name='Mentee'),
    path('db_mentee/', views.db_mentee, name='db_mentee'),
    path('post_new/', views.input_post, name='input_post'),
]