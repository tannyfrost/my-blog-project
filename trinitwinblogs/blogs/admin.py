from django.contrib import admin
from .models import BlogPost, Profile, Blogger


# Register your models here.

# Here we are customising how the model appears on the admin page
@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title','views','blogger','date_created', 'updated',)
    list_filter = ('views', 'date_created','blogger')
    search_fields = ('title',)
    ordering = ('-updated',)
    readonly_fields = ('views',)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['profile','image_preview'] #what we will see in the list view
    readonly_fields = ['image_preview'] 
    fields = ['profile', 'profile_picture', 'image_preview'] #this modifies the arrangement in the expanded view
# admin.site.register(Profile)
    
@admin.register(Blogger)
class BloggerAdmin(admin.ModelAdmin):
    list_display = ['author_name', 'verified']
    # readonly_fields = ['verified']


