from hotel.models import Room
from .availability import check_availability

def get_available_rooms(category, check_in, check_out):
    '''
    function that takes category and returns Room list
    '''
    #now we get list of room objects i.e. queryset of rooms that satisfy the category
    room_list = Room.objects.filter(category=category)

        
        #initializing available rooms list
    available_rooms = []

    # this room adds on or populates available_rooms
    for room in room_list:
        #data contents when the person checks in and when the person checks out
        if check_availability(room, check_in, check_out):
            # we will add the room in the available rooms
            available_rooms.append(room)
    
    #check lentgh of list. 0 means no avilable rooms
    if len(available_rooms) > 0:
        return available_rooms
    else:
        return None