# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Post, Category

# Register your models here.

class PostAdmin(admin.ModelAdmin):
	model = Post
	list_display = ('title', 'pub_date', 'category', 'meta_desc',)

admin.site.register(Post, PostAdmin)
admin.site.register(Category)