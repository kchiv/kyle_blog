from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from posts.models import Post, Category

def home(request):
	posts = Post.objects.order_by('-pub_date')
	return render(request, 'home.html', {'posts':posts})