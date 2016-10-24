# -*- coding: utf8 -*-
from __future__ import unicode_literals
from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class EtudeBiblique(models.Model):
	content = RichTextField()
	titre = models.CharField(max_length=250, blank=True)	
	slug = models.SlugField(max_length=50,)
	def __unicode__(self):
		return self.titre  
	def __str__(self):
		return self.titre



class IntrofuctionEtudeBiblique(models.Model):
	content = RichTextField()
	titre = models.CharField(max_length=250, blank=True)	
	slug = models.SlugField(max_length=50,)
	def __unicode__(self):
		return self.titre  
	def __str__(self):
		return self.titre