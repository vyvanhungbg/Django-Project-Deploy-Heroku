from django.shortcuts import render
from django.http import  HttpResponse
from .models import Post
# Create your views here.
def home(request):
    posts = Post.objects.filter(active=True)[0:3]
    newpost = Post.objects.latest('id')
    context = {'posts':posts, 'newpost':newpost}
    return render(request, 'base/index.html',context)

def posts(request):
    posts = Post.objects.all()
    context = {'posts':posts}
    return render(request, 'base/posts.html',context)

def post(request, pk):
    post = Post.objects.get(id=pk)
    context = {'post':post}
    return render(request, 'base/post.html',context)

def profile(request):
    return render(request, 'base/proflie.html')