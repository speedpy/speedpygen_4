from django.contrib import admin
from mainapp.models import *

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'password']
    search_fields = ['username', 'email', 'password']

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['pk']

@admin.register(ImageCollection)
class ImageCollectionAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name', 'description']

@admin.register(GhibliStyle)
class GhibliStyleAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name', 'description']

@admin.register(StyledImageJob)
class StyledImageJobAdmin(admin.ModelAdmin):
    list_display = ['status']
    search_fields = ['status']
