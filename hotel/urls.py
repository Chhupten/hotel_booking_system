from django.urls import path
from .views import BookingListView, IndexView, RoomListView, BookingListView, RoomDetailView, CancelBookingView, IndexView, AboutUsView
#BookingView
app_name = 'hotel'
#RoomListview is the name which is the given to room list 
urlpatterns = [
    #path('', RoomListView, name='RoomListView'),#home and room_list is same
    path('room_list/', RoomListView, name='RoomListView'),
    #we are using .as_view() function as we cannot use class based views like a normal function-based view
    path('booking_list/',BookingListView.as_view(), name='BookingListView'),
    
    path('room/<category>', RoomDetailView.as_view(), name='RoomDetailView'),   
    path('booking/cancel/<pk>', CancelBookingView.as_view(), name='CancelBookingView'),

    #homepage
    path('', IndexView, name='IndexView'),
    path('about_us', AboutUsView, name='AboutUsView'),
]