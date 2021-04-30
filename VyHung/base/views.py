from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import  HttpResponse

from datetime import date
from datetime import datetime
import datetime as dt

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import PostForm
from .filters import PostFilter
from .models import Post,AboutMe,images
# Create your views here.

def GetDate():
        
        # numberday
        d = dt.date.today()
        someday = dt.date(2019, 6, 27)
        numberday =   d - someday
   
         # Textual month, day and year
        now = datetime.today().strftime("%B %d, %Y |" )
        return now,numberday.days


def home(request):
    posts = Post.objects.all().order_by('-id')[:3]
    aboutme = AboutMe.objects.latest('id')
    Images = images.objects.all()
    now,number_day = GetDate()
    Date = {'now':now, 'number_day':number_day}
    context = {'posts':posts, 'aboutme':aboutme, 'Date':Date, 'Images':Images}
    return render(request, 'base/index.html',context)

def posts(request):
    posts = Post.objects.all()
    myFilter = PostFilter(request.GET,queryset=posts)
    posts = myFilter.qs

    page = request.GET.get('page')

    paginator = Paginator(posts, 5)

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    context = {'posts':posts,'myFilter':myFilter}
    return render(request, 'base/posts.html',context)

def post(request, pk):
    post = Post.objects.get(id=pk)
    context = {'post':post}
    return render(request, 'base/post.html',context)

def profile(request):
    return render(request, 'base/proflie.html')

@login_required(login_url='home')
def createPost(request):
	form = PostForm()

	if request.method == 'POST':
		form = PostForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
		return redirect('posts')

	context = {'form':form}
	return render(request, 'base/post_form.html', context)


def updatePost(request,pk):
    post = Post.objects.get(id=pk)
    form = PostForm(instance=post)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES,instance=post)
        if form.is_valid():
            form.save()
        return redirect('posts')

    context = {'form':form}
    return render(request, 'base/post_form.html', context)


def deletePost(request,pk):
    post = Post.objects.get(id=pk)

    if request.method == 'POST':
        post.delete()
        return redirect('posts')
    context = {'item':post}
    return render(request,'base/delete.html', context)