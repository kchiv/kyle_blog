from __future__ import unicode_literals

from .models import Category, Post

def category_context(request):
	category_cont = Category.objects.order_by('title')
	posts_context = Post.objects.order_by('-pub_date')
	return {'category_cont':category_cont, 'posts_context':posts_context}