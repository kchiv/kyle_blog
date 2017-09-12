from django.contrib.sitemaps import Sitemap
from posts.models import Post, Category

class PostSitemap(Sitemap):
	changefreq = 'monthly'
	priority = 1.0

	def items(self):
		return Post.objects.all()

	def lastmod(self, item):
		return item.pub_date

class CategorySitemap(Sitemap):
	changefreq = 'weekly'
	priority = 0.7

	def items(self):
		return Category.objects.all()