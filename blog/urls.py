from django.contrib import admin
from django.urls import path
from blog import views
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    PostListView,
    UserPostListView
    )
urlpatterns = [
    path('',PostListView.as_view(),name="home"),
    path('post/<int:pk>/',PostDetailView.as_view(),name='post-detail'),
    path('about/',views.about,name="about"),
    path('post/new/',PostCreateView.as_view(),name='post-new'),
    path('post/<int:pk>/update/',PostUpdateView.as_view(),name='post-update'),
    path('post/<int:pk>/delete/',PostDeleteView.as_view(),name='post-delete'),
    path('user/<username>/',UserPostListView.as_view(),name='user-post'),
]
