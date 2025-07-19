from django.db import models
import os
from django.contrib.auth.models import User
from django.utils.html import format_html

# to rename our images uploaded to the name of the blog post
def rename_image(instance, filename):
    # this gets the file's name
    ext = filename.split('.')[-1]
    # this splits the file name by the point and [-1] picks the last one
    new_filename = f"{instance.title}.{ext}"
    # joining the title name with the extension
    return os.path.join('blog_pictures', new_filename)

# to rename our profile picture to the name of our username
def rename_profile_picture(instance, filename):
    # this gets the file's name
    ext = filename.split('.')[-1]
    # this splits the file name by the point and [-1] picks the last one
    new_filename = f"{instance.profile.username}.{ext}"
    # joining the title name with the extension
    return os.path.join('profile_pictures', new_filename)

# our profile class it has a method to preview profile pictures as well
class Profile(models.Model):
    profile = models.OneToOneField(User, on_delete = models.CASCADE)
    # when adding images its better to add a default image
    profile_picture = models.ImageField(upload_to=rename_profile_picture,blank=True, default= 'profile_pictures/default_user.png')

    def __str__(self):        
        return self.profile.username
    
    # this function is to help us preview the image in our admin panel, dont forget to import format_html
    def image_preview(self):
        if self.profile_picture:
            return format_html('<img src="{}" alt="" width="50" height="50" style="object-fit: cover;"/>', self.profile_picture.url)
        return '(No image)'
    
    image_preview.short_description = 'Preview'

# our blogger class
# Note that every blogger has a profile but not every profile is a blogger
class Blogger(models.Model):
    profile =models.OneToOneField(Profile, on_delete=models.CASCADE)
    author_name = models.CharField(max_length = 100, unique = True)
    verified = models.BooleanField(default = False)
    followers = models.PositiveIntegerField(default = 0)

    def __str__(self):
        return self.author_name
    
# the class of our blog posts
class BlogPost(models.Model):
    blogger = models.ForeignKey(Blogger, on_delete = models.CASCADE, default = 1)
    title = models.CharField(max_length=100)
    body = models.TextField()
    summary = models.CharField(max_length = 200)
    # for auto now add, it is created only once when the field is created
    date_created = models.DateTimeField(auto_now_add = True)
    # this is used for tracking last updated
    updated = models.DateTimeField(auto_now = True)
    views = models.PositiveIntegerField(default = 0)
    # for image field you have to install pillow and configure the settings and urls as well
    images = models.ImageField(upload_to=rename_image, blank=True, default='blog_pictures/default_image.jpg')
    # tags = 


    def __str__(self):
        return self.title

class LandingPage(models.Model):
    todays_date = models.DateField(auto_now = True)

    def __str__(self):
        return self.name
    
class Tag(models.Model):
    tag = models.CharField()
    
    




