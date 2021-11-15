from django.contrib import admin

# Register your models here.
from .models import *

class GamesAdmin(admin.ModelAdmin): # класс игры
    list_display = ('id', 'title', 'time_create', 'photo', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('time_create', 'is_published')
    prepopulated_fields = {'slug': ('title',)}

class CategoryAdmin(admin.ModelAdmin):  #класс категории
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'post', 'time_create', 'time_update', 'is_published')
    list_filter = ('time_create', 'time_update', 'is_published')
    list_editable = ('is_published',)
    list_filter = ('time_create', 'is_published')
    search_fields = ('nickname', 'body')


admin.site.register(Games, GamesAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)
