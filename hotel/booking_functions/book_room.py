from hotel.models import Booking, Room

def book_room(request,room, check_in, check_out):
    # Makes a booking object and saves it
    booking = Booking.objects.create(
                #request is for getting the user
                user=request.user,
                room=room,
                # we are passing check_in that is passed into the function as parameter
                #right side check_in is parameter.
                check_in=check_in,
                check_out=check_out,
            )
    booking.save()

    return booking
