from django.db import models
from datetime import datetime
from django.utils import timezone
from django.utils.html import mark_safe
import os, random

now = timezone.now()

def image_path(instance, filename):
    basefilename, file_extension = os.path.splitext(filename)
    chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    randomstr  =''.join((random.choice(chars)))
    _now = datetime.now()

    return 'profile_pic/{year}-{month}-{imageid}-{randomstr}{ext}'.format(
        imageid= instance, basename=basefilename, randomstring=randomstr, ext=file_extension, year=_now.strftime('%Y'), month=_now.strftime('%m'), day=_now.strftime('%d') )
class User(models.Model):
    user_fname = models.CharField(max_length=50, verbose_name='First Name')
    user_lname = models.CharField(max_length=50, verbose_name='Last Name')
    user_email = models.EmailField(verbose_name="User's Email", unique=True, max_length=200)
    user_position = models.CharField(max_length=200, verbose_name='Position')
    user_image = models.ImageField(upload_to=image_path, default='profile_pic/image.jpg')
    
    def image_tag(self):
        return mark_safe('<img scr="/users/media/%s" width="50" height="50" />' % self.user_image)

    
    
    pub_date = models.DateField(default=now)

    def __str__(self):
        return self.user_email