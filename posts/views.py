# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from .models import Post, Category
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

def post_page(request, post_slug, category_slug):
	post = get_object_or_404(Post, slug=post_slug, category__slug=category_slug)
	return render(request, 'posts/post_page.html', {'post':post})

def category_page(request, category_slug):
	posts = Post.objects.filter(category__slug=category_slug).order_by('-pub_date')
	cat_obj = get_object_or_404(Category, slug=category_slug)
	page = request.GET.get('page', 1)
	paginator = Paginator(posts, 4)

	try:
		post_paginate = paginator.page(page)
	except PageNotAnInteger:
		post_paginate = paginator.page(1)
	except EmptyPage:
		post_paginate = paginator.page(paginator.num_pages)

	return render(request, 'posts/category_page.html', {'posts':posts, 'cat_obj':cat_obj, 'post_paginate':post_paginate})

def all_post_page(request):
	posts = Post.objects.order_by('-pub_date')
	page = request.GET.get('page', 1)
	paginator = Paginator(posts, 4)

	try:
		post_paginate = paginator.page(page)
	except PageNotAnInteger:
		post_paginate = paginator.page(1)
	except EmptyPage:
		post_paginate = paginator.page(paginator.num_pages)

	return render(request, 'posts/all_posts_page.html', {'posts':posts, 'post_paginate':post_paginate})