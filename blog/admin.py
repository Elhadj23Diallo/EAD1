from django.contrib import admin
from blog.models import Photo, Blog
from blog.forms import PhotoForm, BlogForm

# Register your models here.

admin.site.register(Photo)
admin.site.register(Blog)