from django.contrib import admin
from .models import User
# Register your models here.

admin.site.register(User)

admin.site.site_title = 'MoodWise Admin Panel'
admin.site.site_header = 'MoodWise Admin Panel'