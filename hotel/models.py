# lets import the module, "model".
from email.policy import default
from django.db import models
#user will be default user from settings so we are importing it from settings
from django.conf import settings
from django.urls import reverse_lazy

# Create your models here.

#we are making room model. It inherites models.model.
class Room(models.Model):
    #We will make a tuple called room_categories
    #this is a nested tuple
    
    # if we want to add a new category, we should add it from here. The right one is human redable one, the left one is the url used for the computer.
    #don't forget to make migrations, migrate, and add the new category from admin panel.
    ROOM_CATEGORIES = (
        ('YAC', 'AC'),
        ('NAC', 'NON AC'),
        ('DEL', 'DELUXE'),
        ('KIN', 'KING'),
        ('QUE', 'QUEEN'),
    )
    number = models.IntegerField() #we will have just numbers. This is room number like 711,etc.
    #number is used for reference for the admin
    #category max length is 3 because we have just three characters here for e.g YAC.
    #left one YAC is going to be stored in the database and right one AC is going to be displayed to us.
    #choices is Room_CATEGORIES which we defined above. 
    category = models.CharField(max_length=3, choices=ROOM_CATEGORIES)
    beds = models.IntegerField()
    #capacity of the room
    capacity = models.IntegerField()
    room_image = models.ImageField(upload_to='upload/', default="")
    


   


    #Def_str_(self): is a python method which is called when we use print/str to convert object into a string.
    # these magic method are called internally while doing ceratin task. Here we will invoke the __str class__
    #if we don't do this then it will show 'room object' and will look confusing
    # we want to display room object in a specific style. 
     
    def __str__(self):
        return f'{self.number}. {self.category} with {self.beds} beds for {self.capacity} people'

#we are creating booking model so that we can book the rooms
class Booking(models.Model):
    
    #we are using predefined AUTH_USER_MODEL from settings
    #on_delete , we will cascade it from models tha tmeans it will delete the record. 
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    #here we will use ForeignKey for room from Room class created above. It will take foreign key from Room.                         
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    #we will use check in date and time and checkout date and time from models.
    check_in = models.DateTimeField()
    check_out = models.DateTimeField()
    # we will define magic method _str__ so that it returns the following format instead of "room object".
    def __str__(self):
        message= f'Room number {self.room.number} booked by {self.user} '
        return message

    def get_room_category(self):
        #we are getting values from the tuple.
        room_categories = dict(self.room.ROOM_CATEGORIES)
        #human readble formart is room_category
        room_category = room_categories.get(self.room.category)
        return room_category

    def get_cancel_booking_url(self):
        return reverse_lazy('hotel:CancelBookingView',args=[self.pk])

class SliderGallery(models.Model):
     name = models.CharField(max_length=15)
     slider_id = models.IntegerField(default=0)
     slider_image1 = models.ImageField(upload_to='slider_gallery/',default="")
     slider_image2 = models.ImageField(upload_to='slider_gallery/',default="")
     slider_image3 = models.ImageField(upload_to='slider_gallery/',default="")
     slider_image4 = models.ImageField(upload_to='slider_gallery/',default="")

     def __str__(self):
        return f'{self.name} with id no. {self.slider_id}'

class RoomImageGallery(models.Model):
     name = models.CharField(max_length=15)
     AC_image = models.ImageField(upload_to='slider_gallery/',default="https://upload.wikimedia.org/wikipedia/commons/thumb/6/6c/No_image_3x4.svg/1280px-No_image_3x4.svg.png")
     NON_AC_image = models.ImageField(upload_to='slider_gallery/',default="https://upload.wikimedia.org/wikipedia/commons/thumb/6/6c/No_image_3x4.svg/1280px-No_image_3x4.svg.png")
     DELUXE_image = models.ImageField(upload_to='slider_gallery/',default="https://upload.wikimedia.org/wikipedia/commons/thumb/6/6c/No_image_3x4.svg/1280px-No_image_3x4.svg.png")
     KING_image = models.ImageField(upload_to='slider_gallery/',default="https://upload.wikimedia.org/wikipedia/commons/thumb/6/6c/No_image_3x4.svg/1280px-No_image_3x4.svg.png")
     QUEEN_image = models.ImageField(upload_to='slider_gallery/',default="https://upload.wikimedia.org/wikipedia/commons/thumb/6/6c/No_image_3x4.svg/1280px-No_image_3x4.svg.png")
     

     
     



    



