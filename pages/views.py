# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from .models import Page

# Create your views here.

def single_page(request, slug):
	page = get_object_or_404(Page, slug=slug)
	return render(request, 'pages/single_page.html', {'page':page})