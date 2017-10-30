from django.contrib.sitemaps import Sitemap
from posts.models import Post, Category
from pages.models import Page

class PostSitemap(Sitemap):
	changefreq = 'monthly'
	priority = 1.0
	protocol = 'https'

	def items(self):
		return Post.objects.all()

	def lastmod(self, item):
		return item.pub_date

	def location(self, item):
		return item.get_absolute_url(protocol)

class CategorySitemap(Sitemap):
	changefreq = 'weekly'
	priority = 0.7
	protocol = 'https'

	def items(self):
		return Category.objects.all()

class PageSitemap(Sitemap):
	changefreq = 'monthly'
	priority = 0.5
	protocol = 'https'

	def items(self):
		return Page.objects.all()