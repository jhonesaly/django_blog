from django.shortcuts import render
from app_blog.models import Post
from django.urls import reverse

# Create your views here.
def home(request):
    posts = Post.objects.all()
    url_home = reverse('home')
    return render(request, 'index.html', {'posts': posts})

def post(request, post_id):
    post = Post.objects.get(pk=post_id)
    return render(request, 'post.html', {'post': post})
