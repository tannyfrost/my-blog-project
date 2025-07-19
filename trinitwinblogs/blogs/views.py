from django.shortcuts import render
from .models import BlogPost

# Create your views here.

def summarizedPost(request):
    posts = BlogPost.objects.select_related('blogger').values('title', 'summary', 'updated', 'blogger__author_name')
    context = {
        'posts':posts
    }
    return render(request, 'blogs/home.html' ,context)
