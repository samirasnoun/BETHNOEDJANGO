# -*- coding: utf8 -*-
from __future__ import unicode_literals
from django.db import models
from ckeditor.fields import RichTextField
import os







def media_upload_files(instance, filename):
	filename, file_extension = os.path.splitext(filename)
	return 'Media_EnseignementsBibliques_{0}/Auteur_{1}/theme_{2}/{3}{4}'.format(instance.type_media, instance.auteur.slug, instance.theme.slug, instance.slug, file_extension)


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
	image = models.FileField(upload_to=media_upload_files, default='')
	
	titre_media = models.CharField(max_length=250, blank=True)
	auteur = models.ForeignKey(Auteur, blank=True,  on_delete=models.CASCADE)
	theme = models.ForeignKey(Theme, blank=True,  on_delete=models.CASCADE)

	def __unicode__(self):
		return self.titre  
	def __str__(self):
		return self.titre
