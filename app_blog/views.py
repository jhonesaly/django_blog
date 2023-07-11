from django.shortcuts import render, HttpResponseRedirect
from app_blog.models import Post, Comment
from app_blog.forms import CommentForm

# Create your views here.
def home(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})

def post(request, post_id):
    post = Post.objects.get(pk=post_id)
    return render(request, 'post.html', {'post': post})

def addcomment(request,id):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            data = Comment()
            data.name = form.cleaned_data['name']
            data.comment = form.cleaned_data['comment']
            data.post_id = id
            data.save()
            return HttpResponseRedirect(url)
    return HttpResponseRedirect(url)    