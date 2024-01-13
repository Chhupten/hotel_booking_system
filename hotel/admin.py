from django.contrib import admin
#we will import room model which we just made.  
from .models import Room, Booking, RoomImageGallery, SliderGallery

# Register your models here.
#we will regisrer our models here that is Room and booking.
admin.site.register(Room)
admin.site.register(Booking)
admin.site.register(SliderGallery)
admin.site.register(RoomImageGallery)
