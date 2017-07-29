# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from .models import Post, Category

# Create your views here.

def post_page(request, post_slug, category_slug):
	post = get_object_or_404(Post, slug=post_slug, category__slug=category_slug)
	return render(request, 'posts/post_page.html', {'post':post})

def category_page(request, category_slug):
	posts = Post.objects.filter(category__slug=category_slug).order_by('-pub_date')
	cat_obj = get_object_or_404(Category, slug=category_slug)
	return render(request, 'posts/category_page.html', {'posts':posts, 'cat_obj':cat_obj})