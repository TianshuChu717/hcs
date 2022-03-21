from django.contrib import admin
from app.models import UserProfile
from app.models import Likes,Goods

class LikeAdmin(admin.ModelAdmin):
    list_play = ('likes_from','likes_to','create_time')

class GoodAdmin(admin.ModelAdmin):
    list_play = ('name','number','like_num','picture','price')

admin.site.register(Likes,LikeAdmin)
admin.site.register(Goods,GoodAdmin)
admin.site.register(UserProfile)