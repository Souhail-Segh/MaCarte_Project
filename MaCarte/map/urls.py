from django.urls import path
from . import views

# urls related to map: add or delete marker, upload a picture from the map
urlpatterns = [
    path('map/', views.map_view, name='map'),
    path('add_marker/', views.add_marker, name='add_marker'),
    path('upload_photo/<int:marker_id>/', views.upload_photo, name='upload_photo'),
    path('delete_marker/<int:marker_id>/', views.delete_marker, name='delete_marker'),
]