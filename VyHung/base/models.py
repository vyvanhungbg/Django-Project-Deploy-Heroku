from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_save
from django.contrib.auth.models import User
from django.dispatch import receiver

    
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys

# Create your models here.
# from gdstorage.storage import GoogleDriveStorage

# Define Google Drive Storage
# gd_storage = GoogleDriveStorage()

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200, blank=True, null=True)
    last_name = models.CharField(max_length=200, blank=True, null=True)
    email = models.CharField(max_length=200)
    profile_pic = models.ImageField(upload_to="profile", default="images/user.jpg")
    bio = models.TextField(null=True, blank=True)
    Facebook = models.CharField(max_length=200,null=True, blank=True)

    def __str__(self):
        name = str(self.first_name)
        if self.last_name:
            name += ' ' + str(self.last_name)
        return name

    def save(self, *args, **kwargs):
        check = False
        if self.profile_pic:

            imageTemproary = Image.open(self.profile_pic)
            if imageTemproary.mode != 'RGB':
                imageTemproary = imageTemproary.convert('RGB')
            # print("_____",imageTemproary.size[0],imageTemproary.format)
            if imageTemproary.size[0] > 700  or imageTemproary.format != 'JPEG':
                outputIoStream = BytesIO()
                imageTemproaryResized = imageTemproary
                imageTemproaryResized.thumbnail((700, 700),
                                                Image.ANTIALIAS)
                imageTemproaryResized.save(outputIoStream, format='JPEG', quality=65)
                outputIoStream.seek(0)
                self.profile_pic = InMemoryUploadedFile(outputIoStream, 'ImageField',
                                                        "%s.jpg" % self.profile_pic.name.split('.')[0], 'image/jpeg',
                                                        sys.getsizeof(outputIoStream), None)
                check = True
                super(Profile, self).save(*args, **kwargs)
        if(check == False):
            super(Profile, self).save(*args, **kwargs)

    


class Tag(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    

class Post(models.Model):
    headline = models.CharField(max_length=200)
    sub_headline  = models.CharField(max_length=200,null = True, blank=True)
    thumbnail = models.ImageField(null = True, blank=True,upload_to="posts",default="images/x.jpg")
    body  = RichTextUploadingField(null = True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    # active = models.BooleanField(default=False)
    # features = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
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

        # super().save(*args, **kwargs)

        if self.thumbnail:

            imageTemproary = Image.open(self.thumbnail)
            if imageTemproary.mode != 'RGB':
                imageTemproary = imageTemproary.convert('RGB')
            if imageTemproary.size[0] != 900  or imageTemproary.format != 'JPEG':
                outputIoStream = BytesIO()
                imageTemproaryResized = imageTemproary
                imageTemproaryResized.thumbnail((900,(self.thumbnail.height)/(self.thumbnail.width)*900), Image.ANTIALIAS)
                imageTemproaryResized.save(outputIoStream , format='JPEG', quality=75)
                outputIoStream.seek(0)
                self.thumbnail = InMemoryUploadedFile(outputIoStream,'ImageField', "%s.jpg" %self.thumbnail.name.split('.')[0], 'image/jpeg', sys.getsizeof(outputIoStream), None)
            
                super(Post, self).save(*args, **kwargs)

    @property
    def created_dynamic(self):
        now = timezone.now()
        return now
    



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
    image = models.ImageField(blank=True, null=True,upload_to="slides",default="/images/x.jpg")

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.image:

            imageTemproary = Image.open(self.image)
            if imageTemproary.mode != 'RGB':
                imageTemproary = imageTemproary.convert('RGB')
            if imageTemproary.size[0] != 550  or imageTemproary.format != 'JPEG':
                outputIoStream = BytesIO()
                imageTemproaryResized = imageTemproary
                imageTemproaryResized.thumbnail((550, (self.image.height)/(self.image.width)*550), Image.ANTIALIAS)
                imageTemproaryResized.save(outputIoStream, format='JPEG', quality=70)
                outputIoStream.seek(0)
                self.image = InMemoryUploadedFile(outputIoStream, 'ImageField', "%s.jpg" % self.image.name.split('.')[0],
                                                'image/jpeg', sys.getsizeof(outputIoStream), None)
                super(images, self).save(*args, **kwargs)


class Music(models.Model):
    music = models.CharField(max_length=100)
    def __str__(self):
        return self.music

class AboutMe(models.Model):
    maxim = models.CharField(max_length=100)
    more_about_me_1 = models.CharField(max_length=200)
    more_about_me_2 =  models.CharField(max_length=200,null = True, blank=True)
    images_slide = models.ManyToManyField(images)
    image_author = models.ImageField(upload_to="author",default="/images/x.jpg")
    headline_favorite = models.CharField(max_length=200,null = True, blank=True)
    favorites =  models.ManyToManyField(favorite)
    songs = models.ManyToManyField(song)
    
    def __str__(self):
        return self.maxim

    def save(self, *args, **kwargs):

        if self.image_author:
            imageTemproary = Image.open(self.image_author)
            if imageTemproary.mode != 'RGB':
                imageTemproary = imageTemproary.convert('RGB')
            if imageTemproary.size[0] != 600  or imageTemproary.format != 'JPEG':
                outputIoStream = BytesIO()
                imageTemproaryResized = imageTemproary
                imageTemproaryResized.thumbnail((600 , (self.image_author.height)/(self.image_author.width)*600),
                                                Image.ANTIALIAS)
                imageTemproaryResized.save(outputIoStream, format='JPEG', quality=80)
                outputIoStream.seek(0)
                self.image_author = InMemoryUploadedFile(outputIoStream, 'ImageField',
                                                        "%s.jpg" % self.image_author.name.split('.')[0], 'image/jpeg',
                                                        sys.getsizeof(outputIoStream), None)
                super(AboutMe, self).save(*args, **kwargs)


class PostComment(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True  )
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True )
    body = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    post_comment = models.CharField(max_length=200,null = True, blank=True) # xac dinh tham chieu toi xem ai cmt
    def __str__(self):
        return self.body
    

    @property
    def created_dynamic(self):
        now = timezone.now()
        return now
    




    





	
    