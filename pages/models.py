# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.template.defaultfilters import slugify
from filer.fields.image import FilerImageField
from filer.fields.file import FilerFileField

# Create your models here.

class Page(models.Model):
	title = models.CharField(max_length=250)
	meta_desc = models.CharField(max_length=200, blank=True)
	header = models.CharField(max_length=200, blank=True)
	pub_date = models.DateTimeField()
	body = models.TextField(blank=True, default='')
	slug = models.SlugField(max_length=60, blank=True)
	custom_css = FilerFileField(null=True, blank=True, related_name="page_css")
	custom_js = FilerFileField(null=True, blank=True, related_name="page_js")

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(self.title)
		if not self.meta_desc:
			self.meta_desc = self.body[:175] + '...'
		if not self.header:
			self.header = self.title
		super(Page, self).save(*args, **kwargs)

	def __str__(self):
		return self.title

	def pub_date_pretty(self):
		return self.pub_date.strftime('%b %d, %Y')

	def summary(self):
		if len(self.body) >= 100:
			return self.body[:100] + '...'
		else:
			return self.body

	def get_absolute_url(self):
		return "/page/%s/" % (self.slug)