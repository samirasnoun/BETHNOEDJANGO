from __future__ import unicode_literals

from django.db import models
from django.contrib import admin

from fields import ThumbnailImageField

# Create your models here.
class ImageAccueil(models.Model):
    AFFI_PAGE_ACCUEIL = (
        ('oui', 'Afficher dans la page Home'),
        ('non', 'Ne pas l afficher dans la page Home'),
    )
    
    title = models.CharField(max_length=100)
    photo =  ThumbnailImageField(upload_to='')
    caption = models.CharField(max_length=250, blank=True)
    afficher = models.CharField(max_length=3, choices=AFFI_PAGE_ACCUEIL, default='oui')
   


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


class ImageBackgroud(ImageAccueil):
    """docstring for ImageBackgroud"""
    
        

@admin.register(ImageAccueil)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'photo', 'caption', 'afficher')
    search_fields = ('title',)


@admin.register(ImageBackgroud)
class ImageBackgroudAdmin(admin.ModelAdmin):
    list_display = ('title', 'photo', 'caption', 'afficher')
    search_fields = ('title',)