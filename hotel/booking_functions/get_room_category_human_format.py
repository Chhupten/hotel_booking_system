from hotel.models import Room

def get_room_category_human_format(category):
    '''
    This function takes computer room and returns human redable format
    '''
    room = Room.objects.all()[0] #we need to get all room object here. because we are using tuple (R00M_CATEGORIES) which is inside room
    room_category = dict(room.ROOM_CATEGORIES).get(category, None) #category is a key .get will get the value in the key
    return room_category


            