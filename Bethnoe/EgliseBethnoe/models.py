from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
from fields import ThumbnailImageField  
import uuid
import data

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
        return str(self.photo).replace        ('.jpg' , '.thumb.jpg')

class FondEcran(Image):
    AFFI_PAGE_ACCUEIL = (
                ('oui', 'Afficher dans la page Home'),
                ('non', 'Ne pas l afficher dans la page Home'),
    )
    afficher = models.CharField(max_length=3, choices=AFFI_PAGE_ACCUEIL, default='oui')
    caption = models.CharField(max_length=250, blank=True)
    class Meta:
        verbose_name = "Fond d ecran"
        verbose_name_plural = "Fonds d ecrans"


class ImageCarrousel(Image):
    AFFI_PAGE_ACCUEIL = (
                ('oui', 'Afficher dans la page Home'),
                ('non', 'Ne pas l afficher dans la page Home'),
    )
    afficher = models.CharField(max_length=3, choices=AFFI_PAGE_ACCUEIL, default='oui')
    caption = models.CharField(max_length=250, blank=True)

class DirigentEgliseBethnoe(models.Model):
    photo = models.OneToOneField(
        Image,
        on_delete=models.CASCADE,
        
        default='',
    )    
    nom = models.CharField(max_length=150, blank=True)
    prenom = models.CharField(max_length=150, blank=True)
    mail = models.EmailField(max_length=150, blank=True)
    role = models.CharField(max_length=250, blank=True)


class TextDirigentEgliseBethnoe(models.Model):
    titre = models.CharField(max_length=50, blank=True)
    texte = models.CharField(max_length=250, blank=True)


class Adresse(models.Model):
    num_rue = models.IntegerField(blank=True)
    TYPE_RUE = (
                ('Bd', 'Boulevard'),
                ('R.', 'Rue'),
    ) 
    type_rue = models.CharField(max_length=2, choices=TYPE_RUE, default='R.')
    nom_rue = models.CharField(max_length=150, blank=True)
    ville = models.CharField(max_length=150, choices=data.VILLES_FRANCE, blank=True)
    code_dep = models.CharField(max_length=150, choices=data.CODE_DEP_FRANCE, default='75')

    class Meta:
        verbose_name = "Adresse de contact de l eglise"
        verbose_name_plural = "Adresse de contact de l eglise"

    
class AdresseSimple(models.Model):
    num_rue = models.IntegerField(blank=True)
    TYPE_RUE = (
                ('Bd', 'Boulevard'),
                ('R.', 'Rue'),
    ) 
    type_rue = models.CharField(max_length=2, choices=TYPE_RUE, default='R.')
    nom_rue = models.CharField(max_length=150, blank=True)
    ville = models.CharField(max_length=150, blank=True)
    code_postale = models.CharField(max_length=150, default='75')
    pays = models.CharField(max_length=150, default='France')

    class Meta:
        verbose_name = "Adresse de contact de l eglise"
        verbose_name_plural = "Adresse de contact de l eglise"

class Annonce(models.Model):
    """docstring for Annonce"""
    title = models.CharField(max_length=100)
    def __init__(self, arg):
        super(Annonce, self).__init__()
        self.arg = arg 

class Post(models.Model):
    title = models.CharField        ('title', max_length=64)
    slug = models.SlugField(max_length=64)
    content = models.TextField        ('content')
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        permissions = (
                    ('view_post', 'Can view post'),
        )
        get_latest_by = 'created_at'

    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return {'post_slug': self.slug}
        