from django.shortcuts import render
from django.http import  HttpResponse
from .models import Post,AboutMe,images
from datetime import date
from datetime import datetime
import datetime as dt
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
    context = {'posts':posts}
    return render(request, 'base/posts.html',context)

def post(request, pk):
    post = Post.objects.get(id=pk)
    context = {'post':post}
    return render(request, 'base/post.html',context)

def profile(request):
    return render(request, 'base/proflie.html')