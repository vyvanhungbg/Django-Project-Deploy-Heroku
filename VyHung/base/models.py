from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_save
from django.contrib.auth.models import User
from django.dispatch import receiver

    

# Create your models here.


class Profile(models.Model):
	user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
	first_name = models.CharField(max_length=200, blank=True, null=True)
	last_name = models.CharField(max_length=200, blank=True, null=True)
	email = models.CharField(max_length=200)
	profile_pic = models.ImageField(null=True, blank=True, upload_to="images", default="/user.png")
	bio = models.TextField(null=True, blank=True)
	twitter = models.CharField(max_length=200,null=True, blank=True)

	def __str__(self):
		name = str(self.first_name)
		if self.last_name:
			name += ' ' + str(self.last_name)
		return name

class Tag(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    

class Post(models.Model):
    headline = models.CharField(max_length=200)
    sub_headline  = models.CharField(max_length=200,null = True, blank=True)
    thumbnail = models.ImageField(blank=True, null=True,upload_to="images",default="x.png")
    body  = RichTextUploadingField(null = True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)
    features = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag)
    likes = models.ManyToManyField(User,blank=True,related_name='post_likes')
    slug = models.SlugField(null=True, blank=True)
    
    def number_of_likes(self):
        return self.likes.count()
    
    def __str__(self):
        return self.headline
    
    def save(self, *args, **kwargs):

        if self.slug == None:
            slug = slugify(self.headline)

            has_slug = Post.objects.filter(slug=slug).exists()
            count = 1
            while has_slug:
                count += 1
                slug = slugify(self.headline) + '-' + str(count) 
                has_slug = Post.objects.filter(slug=slug).exists()

            self.slug = slug

        super().save(*args, **kwargs)
    



class favorite(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class song(models.Model):
    song = models.CharField(max_length=20)

    def __str__(self):
        return self.song
    
class images(models.Model):
    title = models.CharField(max_length=10,null=True)
    image = models.ImageField(blank=True, null=True,upload_to="images",default="x.png")

    def __str__(self):
        return self.title

class AboutMe(models.Model):
    maxim = models.CharField(max_length=100)
    more_about_me_1 = models.CharField(max_length=200)
    more_about_me_2 =  models.CharField(max_length=200,null = True, blank=True)
    images_slide = models.ManyToManyField(images)
    image_author = models.ImageField(blank=True, null=True,upload_to="images",default="x.png")
    headline_favorite = models.CharField(max_length=200,null = True, blank=True)
    favorites =  models.ManyToManyField(favorite)
    songs = models.ManyToManyField(song)
    
    def __str__(self):
        return self.maxim



class PostComment(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True)
    body = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    
    def __str__(self):
        return self.body

    @property
    def created_dynamic(self):
        now = timezone.now()
        return now





    

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(
			user=instance,
			first_name=instance.first_name,
			last_name=instance.last_name,
			email=instance.email,
			)
		print("Profile Created!")


@receiver(post_save, sender=User)
def update_profile(sender, instance, created, **kwargs):
    if created == False:

        instance.profile.first_name = instance.first_name
        instance.profile.last_name = instance.last_name
        instance.profile.email = instance.email
        instance.profile.save()
        print("Profile updated!")


@receiver(pre_save, sender=User)
def update_username(sender, instance, **kwargs):
    instance.username = instance.email
    print("Username updated!", instance.username)




	
    