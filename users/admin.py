from django.contrib import admin
from .models import User
# Register your models here.

admin.site.site_header = "Profiler Admin"
admin.site.site_title = "ProfilerApp admin area"
admin.site.index_title = "Welcome to Profiler App!"
class UserAdmin(admin.ModelAdmin):
    list_display = ['image_tag', 'user_fname', 'user_lname', 'user_email', 'user_position']
    search_fields = ['user_fname', 'user_lname', 'user_email', 'user_position']
admin.site.register(User, UserAdmin)