from django.contrib import admin
from .models import design,Post,Room,Message

# registering the model/table from the firstapp to admin panel i.e /admin page
admin.site.register(design)
admin.site.register(Post)
admin.site.register(Room)
admin.site.register(Message)

