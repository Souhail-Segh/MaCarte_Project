from django.urls import path
from . import views
from .views import clear_unused_categories
from .views import (
    PostListView,
    PostCreateView,
    PostDeleteView,
    UserPostListView
)


''' urls  related to home page, adding and deleting images'''
urlpatterns = [
    path('', PostListView.as_view(), name='gallery-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('photo/<str:pk>/delete/', PostDeleteView.as_view(), name='photo-delete'),
    path('about/', views.about, name='gallery-about'),
    path('photo/<str:pk>/', views.viewPhoto, name='photo'),
    path('add/', views.addPhoto, name='add'),
    path('clear-categories/', clear_unused_categories, name='clear-categories'),    
    
]
