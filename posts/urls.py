from django.conf.urls import url
from django.contrib.sitemaps.views import sitemap
from kyle_blog.sitemaps import PostSitemap, CategorySitemap
from . import views

app_name = 'posts'

post_sitemaps = {
	'posts': PostSitemap,
}

cat_sitemaps = {
	'category': CategorySitemap,
}

urlpatterns = [
	url(r'^(?P<category_slug>[-\w]+)/(?P<post_slug>[-\w]+)/$', views.post_page, name='post_page'),
	url(r'^(?P<category_slug>[-\w]+)/$', views.category_page, name='category_page'),
	url(r'^posts/sitemap\.xml$', sitemap, {'sitemaps': post_sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
	url(r'^category/sitemap\.xml$', sitemap, {'sitemaps': cat_sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]
