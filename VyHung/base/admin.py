from django.contrib import admin

# Register your models here.
from .models import Post,Tag,AboutMe,favorite,song,images

admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(AboutMe)
admin.site.register(favorite)
admin.site.register(song)
admin.site.register(images)