from django.contrib import admin
from .models import Post, Department, Industry, Profile

from tinymce.widgets import TinyMCE
from django.db import models

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content','my_field']
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Post, PostAdmin)


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'sales_point')
    list_filter = ("name",)


admin.site.register(Department, DepartmentAdmin)


class IndustryAdmin(admin.ModelAdmin):
    list_display = ('name', 'focus')
    list_filter = ("name",)


admin.site.register(Industry, IndustryAdmin)

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('firstname',)


admin.site.register(Profile, ProfileAdmin)
