# -*- coding: utf8 -*-
from __future__ import unicode_literals
from django.db import models
from ckeditor.fields import RichTextField
import os

def media_upload_files(instance, filename):
	filename, file_extension = os.path.splitext(filename)
	return 'Media_EnseignementsBibliques_{0}/Auteur_{1}/theme_{2}/{3}{4}'.format(instance.type_media, instance.auteur.slug, instance.theme.slug, instance.slug, file_extension)


def fond_upload(instance, filename):
	filename, file_extension = os.path.splitext(filename)
	return 'Media_EnseignementsBibliques/fond_{0}'.format(file_extension)

def logo_upload(instance, filename):
	filename, file_extension = os.path.splitext(filename)
	return 'Media_EnseignementsBibliques/logo_{0}'.format(file_extension)

def images_upload(instance, filename):
	filename, file_extension = os.path.splitext(filename)
	return 'Media_EnseignementsBibliques/eglise_partenaire_{0}_{1}'.format(instance.slug,file_extension)


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



class Section(models.Model):
    
    ANGLET_SITE = (
                ('EBTNE', 'Eglise Bethnoe'),
                ('EGPTR', 'Eglise partenaire'),
                ('BLKBL', 'Bible en Kabyle'),
                ('ETDBB', 'Etudes bibliques'),
                ('ENSBI', 'Enseignements bibliques'),
                ('LOUAN', 'Louanges'),
                ('FORUM', 'Forum'),
                ('LIENS', 'Liens'),
                ('ACUIL', 'Accueil'),
                

    )
    onglet = models.CharField(max_length=6, choices=ANGLET_SITE, default='EBTNE')
    titre = models.CharField(max_length=250, blank=True)
    content = RichTextField()
    media = models.FileField(upload_to=fond_upload)
    logo = models.FileField(upload_to=fond_upload, default='')
    def __unicode__(self):
    	return self.titre  
    def __str__(self):
    	return self.titre






class EglisePartenaire(models.Model):
    titre = models.CharField(max_length=250, blank=True)	
    content = RichTextField()
    slug = models.SlugField(max_length=50,)
    media = models.FileField(upload_to=images_upload)
    def __unicode__(self):
		return self.titre  
    def __str__(self):
        return self.titre

    class Meta:
        managed = False
        db_table = 'EnseignementsBibliques_eglisepartenaire'