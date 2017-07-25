# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.

def post_details(request, post_id, slug):
	post = get_object_or_404(Post, pk=post_id, slug=slug)
	return render(request, 'posts/post_detail.html', {'post':post})