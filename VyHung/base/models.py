from django.db import models

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    

class Post(models.Model):
    headline = models.CharField(max_length=200)
    sub_headline  = models.CharField(max_length=200,null = True, blank=True)
    thumbnail = models.ImageField(blank=True, null=True,upload_to="images",default="x.png")
    body  = models.TextField(null = True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)
    features = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, null=True)
    #slug = 
    def __str__(self):
        return self.headline

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
    images_slide = models.ManyToManyField(images,null=True)
    image_author = models.ImageField(blank=True, null=True,upload_to="images",default="x.png")
    headline_favorite = models.CharField(max_length=200,null = True, blank=True)
    favorites =  models.ManyToManyField(favorite, null=True)
    songs = models.ManyToManyField(song, null=True)
    
    def __str__(self):
        return self.maxim

    