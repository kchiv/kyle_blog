# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from .models import Page

# Create your views here.

def single_page(request, page_slug):
	page = get_object_or_404(Page, slug=page_slug)
	return render(request, 'pages/page.html', {'page':page})