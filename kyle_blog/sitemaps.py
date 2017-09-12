from django.contrib.sitemaps import Sitemap
from posts.models import Post

class PostSitemap(Sitemap):
	changefreq = 'monthly'
	priority = 1.0

	def items(self):
		return Post.objects.all()

	def lastmod(self, item):
		return item.pub_date