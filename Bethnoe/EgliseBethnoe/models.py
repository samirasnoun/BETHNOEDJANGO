from __future__ import unicode_literals
from django.db import models
from django.contrib import admin
from fields import ThumbnailImageField

# Create your models here.
class Image(models.Model):    
    title = models.CharField(max_length=100)
    photo =  ThumbnailImageField(upload_to='')       
    class Meta:
        ordering = ['title']
    def affiche(self):
        return self.afficher == 'oui'    
    def __unicode__(self):
        return self.title
    def get__absolute_url(self):        
        return str(self.photo)
    def get_url(self):
        return "/images/"  + str(self.id) 
    def get_thumb(self):        
        return str(self.photo).replace('.jpg' , '.thumb.jpg')

class FondEcran(Image):
    AFFI_PAGE_ACCUEIL = (
        ('oui', 'Afficher dans la page Home'),
        ('non', 'Ne pas l afficher dans la page Home'),
    )
    afficher = models.CharField(max_length=3, choices=AFFI_PAGE_ACCUEIL, default='oui')
    caption = models.CharField(max_length=250, blank=True)


class Annonce(models.Model):
    """docstring for Annonce"""
    title = models.CharField(max_length=100)
    def __init__(self, arg):
        super(Annonce, self).__init__()
        self.arg = arg 
        