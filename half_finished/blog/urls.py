from django.urls import path

from . import views

urlpatterns = [
    path('', views.blog, name="blog"),
    path("<path:filename>", views.single, name='single'), 
]
