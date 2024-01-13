import datetime
#we are importing from hotel model both and room and booking
from hotel.models import Room, Booking


def check_availability(room, check_in, check_out):
    #this avail_list will have true or false i.e. boolean
    avail_list = []
    # we are comparing room from bookings to the room in this check_availability function
    # we need to only camprae the same room for eg AC and AC not Ac and Non Ac 
    booking_list = Booking.objects.filter(room=room)
    #we only have to compare it with the same room number so we are using room = room.
    for booking in booking_list:
        #booking.check_in from booking list and check_out from the passed check_in (user entered checkin)
        if check_in<check_out:   
            if booking.check_in > check_out or booking.check_out < check_in:    
                avail_list.append(True)
            else:
                avail_list.append(False)
        else: avail_list.append(False)        
    #return all will return true if all of the items in the list are true.        
    return all(avail_list)
