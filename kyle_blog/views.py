from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from posts.models import Post, Category
from django.shortcuts import render_to_response
from django.template import RequestContext

def home(request):
	posts = Post.objects.order_by('-pub_date')
	return render(request, 'home.html', {'posts':posts})

def handler404(request):
	response = render_to_response('404.html', {}, context_instance=RequestContext(request))
	response.status_code = 404
	return response