from django.conf.urls import url
from django.contrib.sitemaps.views import sitemap
from kyle_blog.sitemaps import PostSitemap
from . import views

app_name = 'posts'

sitemaps = {
	'posts': PostSitemap,
}

urlpatterns = [
	url(r'^(?P<category_slug>[-\w]+)/(?P<post_slug>[-\w]+)/$', views.post_page, name='post_page'),
	url(r'^(?P<category_slug>[-\w]+)/$', views.category_page, name='category_page'),
	url(r'^posts/sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]
