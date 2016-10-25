# -*- coding: utf8 -*-
from __future__ import unicode_literals
from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

def media_upload_files(instance, filename):
	return 'Testament_{0}/Livre_{1}/Chapitre_{2}'.format(instance.livre.type_na, instance.livre.slug, instance.slug)


class Auteur(models.Model):
	nom = models.CharField(max_length=250, blank=True)
	prenom = models.CharField(max_length=250, blank=True)
	slug = models.SlugField(max_length=50,)
	def __unicode__(self):
		return self.nom + " " + self.prenom  
	def __str__(self):
		return self.nom + " " + self.prenom 	


class Theme(models.Model):
	titre = models.CharField(max_length=250, blank=True)
	slug = models.SlugField(max_length=50,)
	def __unicode__(self):
		return self.titre  
	def __str__(self):
		return self.titre	

class EnseignementBiblique(models.Model):
	TYPE_MEDIA = (
        ('AD', 'Audio'),
        ('VI', 'Vidéo'),)
	type_media = models.CharField(max_length=2, choices=TYPE_MEDIA, default='vi')
	content = RichTextField()
	titre = models.CharField(max_length=250, blank=True)	
	slug = models.SlugField(max_length=50,)
	media = models.FileField(upload_to=media_upload_files)
	titre_media = models.CharField(max_length=250, blank=True)
	auteur = models.ForeignKey(Auteur, blank=True,  on_delete=models.CASCADE)
	theme = models.ForeignKey(Theme, blank=True,  on_delete=models.CASCADE)
	def __unicode__(self):
		return self.titre  
	def __str__(self):
		return self.titre
