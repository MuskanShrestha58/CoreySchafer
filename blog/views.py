from django.shortcuts import render
from .models import Post


# Create your views here.

def home(request):
    context = {
        'posts': Post.objects.all()  # Post bhaneko chai model ho
    }

    return render(request, 'blog/home.html', context)


def about(request):

    return render(request, 'blog/about.html', {'title': 'About'})
