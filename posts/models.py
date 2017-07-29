# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.template.defaultfilters import slugify

# Create your models here.

class Category(models.Model):
	title = models.CharField(max_length=100, db_index=True, unique=True)
	image = models.ImageField(upload_to='media/', blank=True, null=True)
	body = models.TextField(blank=True, default='')
	slug = models.SlugField(max_length=100, db_index=True, blank=True, unique=True)

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(self.title)
		super(Category, self).save(*args, **kwargs)

	def __str__(self):
		return self.title

class Post(models.Model):
	title = models.CharField(max_length=250, unique=True)
	pub_date = models.DateTimeField()
	image = models.ImageField(upload_to='media/', blank=True, null=True)
	body = models.TextField(blank=True, default='')
	slug = models.SlugField(max_length=100, blank=True, unique=True)
	category = models.ForeignKey(Category, default=0)

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