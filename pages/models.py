# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.template.defaultfilters import slugify
from filebrowser.fields import FileBrowseField

# Create your models here.

class Page(models.Model):
	title = models.CharField(max_length=250)
	meta_desc = models.CharField(max_length=200, blank=True)
	header = models.CharField(max_length=200, blank=True)
	pub_date = models.DateTimeField()
	image = FileBrowseField("Image", max_length=200, directory="uploads/", extensions=[".jpg", ".jpeg"], blank=True, null=True)
	body = models.TextField(blank=True, default='')
	slug = models.SlugField(max_length=60, blank=True)

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
		return self.pub_date.strftime('%b %m, %Y')

	def summary(self):
		if len(self.body) >= 100:
			return self.body[:100] + '...'
		else:
			return self.body