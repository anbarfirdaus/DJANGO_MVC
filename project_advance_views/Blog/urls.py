from django.urls import path
from . import views

urlpatterns = [
    path('', views.Blog, name='Blog'),
    path('db_blog/', views.db_blog, name='db_blog'),
    path('new_post_blog/', views.input_post, name='input_post'),
]


