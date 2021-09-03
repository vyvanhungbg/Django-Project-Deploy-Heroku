from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import  HttpResponse, HttpResponseRedirect
from django.urls import reverse

from datetime import date
from datetime import datetime
import datetime as dt
from django.views.generic import RedirectView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import PostForm,CustomUserCreationForm, ProfileForm, UserForm
from .filters import PostFilter
from .models import Post,AboutMe,images,Profile,Music

from django.views.generic import DetailView
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string

from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .decorators import *


from .filters import PostFilter

from .models import *

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
	posts = Post.objects.all().order_by('-id')[:3] #-id sap xep nguoc khac id
	aboutme = AboutMe.objects.latest('id')
	Images = images.objects.all()
	now,number_day = GetDate()
	Date = {'now':now, 'number_day':number_day}
	music = Music.objects.latest('id')
	context = {'posts':posts, 'aboutme':aboutme, 'Date':Date, 'Images':Images,'music':music}
	return render(request, 'base/index.html',context)

def posts(request):
    posts = Post.objects.all().order_by('-id')
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

def post(request, slug):
	post = Post.objects.get(slug=slug)

	if request.method == 'POST':
		PostComment.objects.create(
			author=request.user.profile,
			post=post,
			body=request.POST['comment'],
			post_comment= request.user.username
			)
		messages.success(request, "You're comment was successfuly posted!")

		return redirect('post', slug=post.slug)
	
	context = {'post':post}
	return render(request, 'base/post.html',context)

def postLike(request, slug):
	post = Post.objects.get(slug=slug)
	if request.method == 'POST':
		if post.likes.filter(id=request.user.id).exists():
			post.likes.remove(request.user)
		else:
			post.likes.add(request.user)
	return redirect('posts')  # trick load lại trang sau khi cap nhat csdl like

def postLikeIndex(request, slug):
	post = Post.objects.get(slug=slug)
	if request.method == 'POST':
		if post.likes.filter(id=request.user.id).exists():
			post.likes.remove(request.user)
		else:
			post.likes.add(request.user)
	return redirect('home')  # trick load lại trang sau khi cap nhat csdl like

def LikeThisPost(request, slug):
	post = Post.objects.get(slug=slug)
	if request.method == 'POST':
		if post.likes.filter(id=request.user.id).exists():
			post.likes.remove(request.user)
		else:
			post.likes.add(request.user)
	return redirect('post', slug=post.slug)  # trick load lại trang sau khi cap nhat csdl like

def profile(request):
	return render(request, 'base/profile.html')



#CRUD VIEWS
@admin_only
@login_required(login_url="home")
def createPost(request):
	form = PostForm()

	if request.method == 'POST':
		form = PostForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
		return redirect('posts')

	context = {'form':form}
	return render(request, 'base/post_form.html', context)


@admin_only
@login_required(login_url="home")
def updatePost(request, slug):
	post = Post.objects.get(slug=slug)
	form = PostForm(instance=post)

	if request.method == 'POST':
		form = PostForm(request.POST, request.FILES, instance=post)
		if form.is_valid():
			form.save()
		return redirect('posts')

	context = {'form':form}
	return render(request, 'base/post_form.html', context)

@admin_only
@login_required(login_url="home")
def deletePost(request, slug):
	post = Post.objects.get(slug=slug)

	if request.method == 'POST':
		post.delete()
		return redirect('posts')
	context = {'item':post}
	return render(request, 'base/delete.html', context)



def sendEmail(request):
    if request.method == 'POST':
    
        template = render_to_string('base/email_template.html',{
            'name':request.POST['name'],
            'email':request.POST['email'],
            'message' :request.POST['message'],
            })
        email = EmailMessage(request.POST['subject'],
        template,
        settings.EMAIL_HOST_USER,
        ['mystorypagemanagement@gmail.com']
        )
        email.fail_silently=False
        email.send()
    return render(request, 'base/email_sent.html')

def loginPage(request):
	if request.user.is_authenticated:
		return redirect('home')

	if request.method == 'POST':
		email = request.POST.get('email')
		password =request.POST.get('password')

		#Little Hack to work around re-building the usermodel
		try:
			user = User.objects.get(email=email)
			user = authenticate(request, username=user.username, password=password)
		except:
			messages.error(request, 'User with this email does not exists')
			return redirect('login')
			
		if user is not None:
			login(request, user)
			return redirect('home')
		else:
			messages.error(request, 'Email OR password is incorrect')

	context = {}
	return render(request, 'base/login.html', context)

def registerPage(request):
	form = CustomUserCreationForm()
	if request.method == 'POST':
		form = CustomUserCreationForm(request.POST)
		
		if form.is_valid():
			user = form.save(commit=False)
			user.save()
			messages.success(request, 'Account successfuly created!')

			user = authenticate(request, username=user.username, password=request.POST['password1'])

			if user is not None:
				login(request, user)

			next_url = request.GET.get('next')
			if next_url == '' or next_url == None:
				next_url = 'home'
			return redirect(next_url)
		else:
			messages.error(request, 'An error has occured with registration')
	context = {'form':form}
	return render(request, 'base/register.html', context)

def logoutUser(request):
	logout(request)
	return redirect('home')

@login_required(login_url="home")
def userAccount(request):
	profile = request.user.profile
	countLike = Post.objects.filter(likes=request.user).count()
	countComment = PostComment.objects.filter(post_comment=request.user).count()
	numberOfPost = Post.objects.all().count()
	context = {'profile':profile, 'number_post_like':countLike,'countComment':countComment,'numberOfPost':numberOfPost}
	return render(request, 'base/account.html', context)

@login_required(login_url="home")
def updateProfile(request):
	user = request.user
	profile = user.profile
	form = ProfileForm(instance=profile)
	if request.method == 'POST':
		user_form = UserForm(request.POST, instance=user)
		if user_form.is_valid():
			user_form.save()

		form = ProfileForm(request.POST, request.FILES, instance=profile)
		if form.is_valid():
			form.save()
			return redirect('account')


	context = {'form':form}
	return render(request, 'base/profile_form.html', context)