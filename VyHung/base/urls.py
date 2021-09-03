from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('posts/', views.posts, name='posts'),
    path('post/<slug:slug>/', views.post, name='post'),
    path('postLike/<slug:slug>/', views.postLike, name='postLike'),
    path('postLikeIndex/<slug:slug>/', views.postLikeIndex, name='postLikeIndex'), #Like Index
    path('LikeThisPost/<slug:slug>/', views.LikeThisPost, name='LikeThisPost'), #Like this post
    path('profile/', views.profile, name='profile'),
    path('create_post/', views.createPost, name='create_post'),
    path('update_post/<slug:slug>/', views.updatePost, name='update_post'),
    path('delete_post/<slug:slug>/', views.deletePost, name='delete_post'),
    path('send_email/', views.sendEmail, name='send_email'),

    path('login/', views.loginPage, name="login"),
	path('register/', views.registerPage, name="register"),
	path('logout/', views.logoutUser, name="logout"),

	path('account/', views.userAccount, name="account"),
	path('update_profile/', views.updateProfile, name="update_profile"),
]
