from django.contrib import admin
from .models import UserProfile

class userprofile(admin.ModelAdmin):
    list_display = ['user', 'gender', 'phone','update_time',]
admin.site.register(UserProfile, userprofile)
