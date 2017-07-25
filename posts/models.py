# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.template.defaultfilters import slugify

# Create your models here.

class Post(models.Model):
	title = models.CharField(max_length=250)
	pub_date = models.DateTimeField()
	image = models.ImageField(upload_to='media/', blank=True, default='')
	body = models.TextField(blank=True, null=True)
	slug = models.SlugField(max_length=60, blank=True)

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(self.title)
		super(Post, self).save(*args, **kwargs)

	def __str__(self):
		return self.title

	def pub_date_pretty(self):
		return self.pub_date.strftime('%b %m, %Y')

	def summary(self):
		if len(self.body) >= 100:
			return self.body[:100] + '...'
		else:
			return self.body