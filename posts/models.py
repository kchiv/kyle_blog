# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.template.defaultfilters import slugify
from filer.fields.image import FilerImageField
from filer.fields.file import FilerFileField

# Create your models here.

class Category(models.Model):
	title = models.CharField(max_length=100, db_index=True, unique=True)
	meta_desc = models.CharField(max_length=200, blank=True)
	header = models.CharField(max_length=200, blank=True)
	featured_image = FilerImageField(null=True, blank=True, related_name="cat_featured_image")
	body = models.TextField(blank=True, default='')
	slug = models.SlugField(max_length=100, db_index=True, blank=True, unique=True)

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(self.title)
		if not self.meta_desc:
			self.meta_desc = self.body[:175] + '...'
		if not self.header:
			self.header = self.title
		super(Category, self).save(*args, **kwargs)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return "/blog/%s/" % self.slug

class Post(models.Model):
	title = models.CharField(max_length=250, unique=True)
	meta_desc = models.CharField(max_length=200, blank=True)
	header = models.CharField(max_length=200, blank=True)
	featured_image = FilerImageField(null=True, blank=True, related_name="post_featured_image")
	pub_date = models.DateTimeField()
	body = models.TextField(blank=True, default='')
	slug = models.SlugField(max_length=100, blank=True, unique=True)
	category = models.ForeignKey(Category, default=0)
	custom_css = FilerFileField(null=True, blank=True, related_name="post_css")
	custom_js = FilerFileField(null=True, blank=True, related_name="post_js")

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(self.title)
		if not self.meta_desc:
			self.meta_desc = self.body[:175] + '...'
		if not self.header:
			self.header = self.title
		super(Post, self).save(*args, **kwargs)

	def __str__(self):
		return self.title

	def pub_date_pretty(self):
		return self.pub_date.strftime('%b %m, %Y')

	def pub_date_og(self):
		return self.pub_date.strftime('%Y-%m-%dT%H:%M:%SZ')

	def summary(self):
		if len(self.body) >= 100:
			return self.body[:200] + '...'
		else:
			return self.body

	def get_absolute_url(self):
		return "/blog/%s/%s/" % (self.category.slug, self.slug)