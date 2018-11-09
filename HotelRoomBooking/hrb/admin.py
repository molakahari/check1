from django.contrib import admin
from hrb.models import Rooms,hotelusers,urequests
# Register your models here.
class RoomsAdmin(admin.ModelAdmin):
    list_display=('roomno','roomtype','bedtype','status')
class hotelusersAdmin(admin.ModelAdmin):
    list_display=['username']

class urequestsAdmin(admin.ModelAdmin):
    list_display=['name','roomtype','bedtype','mobile','email']
admin.site.register(Rooms,RoomsAdmin)
admin.site.register(hotelusers,hotelusersAdmin)
admin.site.register(urequests,urequestsAdmin)


from django.contrib.auth.models import User, Group


admin.site.unregister(User)
admin.site.unregister(Group)
