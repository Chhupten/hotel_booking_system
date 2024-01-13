# we are importing Room model because we are using it in this function. 
from hotel.models import Room
from django.urls import reverse


def get_room_cat_url_list():
    '''
    This function returns Room Category and category url list 
    '''

    room = Room.objects.all()[0] # we are the first "Room" object with [0]
    #print('categories=',room_categories)
    # we are making dictionary out of the ROOM_CATEGORIES. 
    room_categories = dict(room.ROOM_CATEGORIES)
    #room_values = room_categories.values()
    #print('categories=',room_values)
    room_cat_url_list = [] # we are initializing empty room category and url list.
    
    
    #this for loop generates the room list 
    # we are passing categories not rooms. we are passing ac/ non ac etc. so we should pass category which is computer format
    for category in room_categories:   # for loop for adding into the room_cat_url_list
        #room_category is human redable catagory here. It is the value. category is the key which is read by computer.
        # we are getting value assigned to the specific key 
        #room_category is human readable format as we used .get()
        room_category = room_categories.get(category)
        room_url = reverse('hotel:RoomDetailView', kwargs={
                            'category': category})
        #room_url is for computer and room_category is for human                 
        #print(room, room_url)
        # we are taking the room category and passing into the room_cat_url_list.
        # we are appending it into the tuple
        room_cat_url_list.append((room_category,room_url))
    
    return room_cat_url_list
      
    
