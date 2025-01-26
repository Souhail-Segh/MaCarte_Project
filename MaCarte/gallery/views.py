from django.shortcuts import render, redirect
from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Category, Photo, Marker
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.generic import (
    ListView, 
    CreateView,
    DeleteView
    )
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Number of photos to display in one page
PAGES_NUMBER = 6

# home page
def home(request):
    category = request.GET.get('category')

    
    if category == None:
        photos = Photo.objects.all()
    else:
        photos = Photo.objects.filter(category__name=category)

    if request.user.is_authenticated:
        photos = photos.filter(user=request.user)  # Use the user object directly to filter
    else:
        photos = None  # No photos available for anonymous users

    
    categories = Category.objects.all()
    context = {'categories': categories, 'photos': photos}
    
    return render(request, 'gallery/gallery.html',context)

# page to see one selected photo
def viewPhoto(request, pk):
    photo = Photo.objects.get(id=pk)
    context = {'photo': photo} 
    
    return render(request, 'gallery/photo.html', context)


# page with a form for adding photo, with category and description
def addPhoto(request):
    marker_id = request.GET.get('marker_id')
    marker = None

    # Try to get the marker if marker_id is provided
    if marker_id:
        marker = get_object_or_404(Marker, id=marker_id)

    if request.method == 'POST':
        data = request.POST
        image = request.FILES.get('image')

        # Handle category selection or creation
        if data['category'] != 'none':
            category = get_object_or_404(Category, id=data['category'])
        elif data['category_new'] != '':
            category, created = Category.objects.get_or_create(name=data['category_new'])
        else:
            category = None

        # Create the Photo and associate it with the Marker (if available)
        photo = Photo.objects.create(
            user = request.user,
            category=category,
            description=data['description'],
            image=image,
            marker=marker  # Associate with marker only if it exists
        )

        # Update the marker's last_photo field (if marker exists)
        if marker:
            marker.last_photo = photo
            marker.save()

        # Redirect to the home page
        return redirect('gallery-home')

    return render(request, 'gallery/add.html')


# This class allow structuring album as to show only PAGES_NUMBER * pictures
class PostListView(LoginRequiredMixin, ListView):
    model = Photo
    template_name = 'gallery/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'photos'
    ordering = ['-date_posted']
    paginate_by = PAGES_NUMBER

    def get_queryset(self):
        queryset = Photo.objects.all()

        # Filter by category (if provided in the query params)
        category = self.request.GET.get('category')
        if category:
            queryset = queryset.filter(category__name=category)

        # Filter by the authenticated user
        if self.request.user.is_authenticated:
            queryset = queryset.filter(user=self.request.user)

        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()  # Add categories to the context
        return context

class UserPostListView(ListView):
    model = Photo
    template_name = 'gallery/user_posts.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = PAGES_NUMBER

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Photo.objects.filter(author=user).order_by('-date_posted')

# Class for creating new picture 
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Photo
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
# Class for deleting a specific picture
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Photo
    success_url = reverse_lazy('gallery-home')  # Redirect to the home page after deletion
    template_name = 'gallery/confirm_delete.html'  # Optional: add a confirmation template

    def test_func(self):
        # Ensure only the owner of the photo can delete it
        photo = self.get_object()
        return self.request.user == photo.user

# About MaCarte view
def about(request):
    return render(request, 'gallery/about.html', {'title':'About'})

# To clean category if no longer a picture mention it
@login_required
def clear_unused_categories(request):
    if request.method == 'POST':
        unused_categories = Category.objects.filter(photo__isnull=True)
        unused_categories.delete()
        return redirect('gallery-home')