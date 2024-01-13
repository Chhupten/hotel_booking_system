from re import I
from django.shortcuts import render, HttpResponse, redirect
#import list view from django. list view in django displays the objects/entries in the database. 
from django.views.generic import ListView, FormView, View, DeleteView
# we are import our Room and Booking model.
from .models import Room, Booking, RoomImageGallery, SliderGallery
from .forms import AvailabilityForm
from hotel.booking_functions.availability import check_availability
#reverse should be imported because it is not a bulit in function
from django.urls import reverse, reverse_lazy
# we are importing the get_room_list function. 
from hotel.booking_functions.get_room_cat_url_list import get_room_cat_url_list
from hotel.booking_functions.get_room_category_human_format import get_room_category_human_format
from hotel.booking_functions.get_available_rooms import get_available_rooms
from hotel.booking_functions.book_room import book_room


# Python 3.x code
# Imports
import tkinter
from tkinter import messagebox

# This code is to hide the main tkinter window
root = tkinter.Tk()
root.withdraw()


# Create your views here.


def RoomListView(request):
    #to make it clear for viewer
    room_category_url_list = get_room_cat_url_list()
    room_image_gallery = RoomImageGallery.objects.all()[0]
    #room_image = Room.obejetcs.room_image
        
    #current_room = room_list[0]
    
    context={

        "room_list": room_category_url_list,
        "room_image_gallery": room_image_gallery

    }
    return render(request, 'room_list_view.html', context)


#this returns all the bookings of the user
class BookingListView(ListView):
        
        #Booking is a class/model from models.py
        model = Booking
        #check if staff or not
        def get_queryset(self, *args, **kwargs):
                if self.request.user.is_staff:
                    booking_list = Booking.objects.all()
                    #print(booking_list)
                    return booking_list
                    
                else:
                    #filter only bookings you have booked
                    booking_list = Booking.objects.filter(user=self.request.user)
                    return booking_list


class RoomDetailView(View):
    
    #RoomDetailView is generic view based . It inherits from generic view
    #*args -> Represents a List / Tuple of positional arguments to be passed to any function
    #*args is commonly used when you’re not sure about the number of arguments that you want to pass as function parameters, when you define the function.
    #**kwargs -> Represents a Dictionary of keyword arguments to be passed to any function
    
    def get(self, request, *args, **kwargs):

        #get room category from keyword arguments (kwargs)
        category = self.kwargs.get('category', None)

        #get the human readable format
        human_format_room_category= get_room_category_human_format(category)
        
        form = AvailabilityForm()
        # we are doing this to get room object for displaying images.
        #category=category is filtering only the room matching with keyword arguments with room object category
        room_list = Room.objects.filter(category=category)
        #checking if category name is valid
        if human_format_room_category is not None:
            current_room = room_list[0]
            context = {
                'room_category': human_format_room_category,
                'form': form, #form is the availability form
                #getting room for displaying in description of room details
                'current_room': current_room,
        }
        #context, A dictionary of values to add to the template context. By default, this is an empty dictionary. 
        # If a value in the dictionary is callable, the view will call it just before rendering the template.
            #request is needed to pass as it store the path
            return render(request, 'room_detail_view.html', context)
        else:
            return render(request, 'category_not_exist.html', context)

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            category = self.kwargs.get('category', None) #this gets the keyword argument from address bar. i.e for eg. NAC 
            
            #simply assigning availability form to form. We are also passing request.POST into avuialbility form
            form = AvailabilityForm(request.POST)
            #cleaned data creates a dictionary which containins cleaned data from field which have passed validation test.
            if form.is_valid():
                data = form.cleaned_data
            # we will get available rooms from this function
            available_rooms = get_available_rooms(category, data['check_in'], data['check_out'])

            if available_rooms is not None:
                # book first available room
                booking = book_room(request, available_rooms[0], data['check_in'], data['check_out']) #we are using square bracket notation because data is in form of dictionary
                # if there are any available rooms then we book the room    
                # and we will return the booking
                return render(request, 'booking_success.html')
            else: 
                return render(request, 'booking_fail.html')
        else :
            return redirect('/accounts/login/')


#class BookingView(FormView):
#    form_class = AvailabilityForm
#    template_name = 'availability_form.html'
#
#    def form_valid(self, form):
        data = form.cleaned_data
        room_list = Room.objects.filter(category=data['room_category'])
        available_rooms = []
        for room in room_list:
            if check_availability(room, data['check_in'], data['check_out']):
                available_rooms.append(room)

        if len(available_rooms) > 0:
            room = available_rooms[0]
            booking = Booking.objects.create(
                user=self.request.user,
                room=room,
                check_in=data['check_in'],
                check_out=data['check_out']
            )
            return HttpResponse(booking)
        else:
            return HttpResponse('All of this category of rooms are booked!! Try another one')
#this class based view will inherit from delete view
# we are using reverse_lazuy beacuse it is used for class to return object. reverse is used in functions to return string
class CancelBookingView(DeleteView):
    model = Booking
    template_name = 'booking_cancel_view.html'
    success_url = reverse_lazy('hotel:BookingListView') 

#home page view

def IndexView(request):
    slider_gallery = SliderGallery.objects.all()[0]
    context={
        "slider_gallery": slider_gallery
    }
    return render(request, 'index.html', context)


#about us page view

def AboutUsView(request):
    return render(request, 'about_us.html')

def csrf_failure(request, reason=""):
    ctx = {'message': 'some custom messages'}
    return HttpResponse("csrf_failure happens sometimes. Please go back and try again. Maybe Cookies are diasbled? Please note that django does this for your own security.")