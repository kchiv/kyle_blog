# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from .models import Post, Category

# Create your views here.

def post_page(request, post_slug, category_slug):
	post = get_object_or_404(Post, post_slug=slug, category_slug=category.slug)
	return render(request, 'posts/post_page.html', {'post':post})

def category_page(request, slug):
	posts = Post.objects.order_by('-pub_date')
	return render(request, 'posts/post_page.html', {'post':post})