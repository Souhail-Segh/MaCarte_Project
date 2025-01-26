from django.utils import timezone
from django.db import models
from users.models import User


''' ORM Models'''
# Category Model
class Category(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name

# Marker Model - map markers
class Marker(models.Model):
    name = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.name
    
user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="photos")
    
# Photo Model    
class Photo(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    date_posted = models.DateTimeField(default=timezone.now)
    description = models.TextField()
    marker = models.ForeignKey(Marker, related_name="photos", on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="photos")  # Relate Photo to the User model

    def __str__(self):
        user_name = self.user.username if self.user else "Anonymous"
        marker_name = self.marker.name if self.marker else "No Marker"
        return f"Photo for {marker_name} by {user_name}"
