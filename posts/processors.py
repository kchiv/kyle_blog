from __future__ import unicode_literals

from .models import Category

def category_context(request):
	category = Category.objects.order_by('title')
	return {'category':category}