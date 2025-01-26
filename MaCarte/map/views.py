from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from gallery.models import Marker, Photo
from django.core.files.storage import FileSystemStorage 
import json


# Create your views here.
def map_view(request):
    markers = Marker.objects.all()
    markers_data = [
        {"id": marker.id, "name": marker.name, "latitude": marker.latitude, "longitude": marker.longitude, 
         "photo": Photo.objects.filter(marker_id=marker.id).last().image.url if Photo.objects.filter(marker_id=marker.id).exists() else None }
        for marker in markers
    ]
    return render(request, 'map/map.html', {'markers': json.dumps(markers_data), 'jsmap':True})

@csrf_exempt
def add_marker(request):
    if request.method == 'POST':
        data = request.POST
        name = data.get('name', 'Unnamed Location')  # Default to "Unnamed Location" if name is empty
        latitude = float(data.get('latitude'))
        longitude = float(data.get('longitude'))

        # Create the new marker
        marker = Marker.objects.create(name=name, latitude=latitude, longitude=longitude)

        # Return data in the same format as map_view
        return JsonResponse({
            "marker_id": marker.id,
            "name": marker.name,
            "latitude": marker.latitude,
            "longitude": marker.longitude,
            "photo": None  # No photos available for a new marker
        })

@csrf_exempt
def upload_photo(request, marker_id):
    try:
        marker = Marker.objects.get(id=marker_id)
    except Marker.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'Marker not found'})

    if request.method == 'POST' and 'image' in request.FILES:
        image = request.FILES['image']
        photo = Photo.objects.create(marker=marker, image=image)

        # Return the URL of the uploaded photo
        return JsonResponse({'success': True, 'photo_url': photo.image.url})

    # If no photo was uploaded
    last_photo = marker.photos.last()
    last_photo_url = last_photo.image.url if last_photo else None
    return JsonResponse({'success': True, 'last_photo_url': last_photo_url})

@csrf_exempt
def delete_marker(request, marker_id):
    if request.method == 'POST':
        try:
            marker = Marker.objects.get(id=marker_id)
            marker.delete()
            return JsonResponse({'success': True})
        except Marker.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Marker not found'})