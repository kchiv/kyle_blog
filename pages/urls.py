from django.conf.urls import url
from django.contrib.sitemaps.views import sitemap
from kyle_blog.sitemaps import PageSitemap
from . import views

app_name = 'pages'

page_sitemaps = {
	'pages': PageSitemap,
}

urlpatterns = [
	url(r'^(?P<page_slug>[-\w]+)/$', views.single_page, name='single_page'),
	url(r'^sitemap\.xml$', sitemap, {'sitemaps': page_sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]