from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from app_blog.models import Post, Comment
from app_blog.forms import CommentForm

# Create your views here.
def home(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})

def post(request, post_id):
    post = Post.objects.get(pk=post_id)
    form = CommentForm()
    return render(request, 'post.html', {'post': post, 'form':form})

def addcomment(request, post_id=None):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            data = Comment()
            data.name = form.cleaned_data['name']
            data.comment = form.cleaned_data['comment']
            data.post = Post.objects.get(pk=post_id)
            data.save()
    return HttpResponseRedirect(reverse('post', args=[post_id]))
