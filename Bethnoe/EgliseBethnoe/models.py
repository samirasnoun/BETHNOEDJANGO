# -*- coding: utf8 -*- 
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
from fields import ThumbnailImageField  
import uuid
import data , os
from ckeditor.fields import RichTextField
from django.core.validators import RegexValidator

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
        verbose_name = "Page d'accueil : Fond d ecran"
        verbose_name_plural = "Page d'accueil : Fonds d ecrans"


class ImageCarrousel(Image):
    AFFI_PAGE_ACCUEIL = (
                ('oui', 'Afficher dans la page Home'),
                ('non', 'Ne pas l afficher dans la page Home'),
    )
    afficher = models.CharField(max_length=3, choices=AFFI_PAGE_ACCUEIL, default='oui')
    caption = models.CharField(max_length=250, blank=True)
    class Meta:
        verbose_name = "Page d'accueil : image du carousel de la page d'accueil"
        verbose_name_plural = "Page d'accueil : Images du carousel de la page d'accueil"    

class DirigentEgliseBethnoe(models.Model):
    photo = models.OneToOneField(
        Image,
        on_delete=models.CASCADE,
        
        default='',
    )    
    nom = models.CharField('Nom de la section du site à mettre en valeur ', max_length=150, blank=True)
    role = models.CharField('Sous texte', max_length=250, blank=True)
    lien = models.URLField('Url sur laquelle pointe le role' , )
    class Meta:
        verbose_name="Page d'accueil : Liens - sections à mettre en valeurs "
        verbose_name_plural="Page d'accueil : Liens - sections à mettre en valeurs "




class TextDirigentEgliseBethnoe(models.Model):
    titre = models.CharField(max_length=50, blank=True)
    texte = models.CharField(max_length=250, blank=True)
    class Meta:
        verbose_name = "Page d'accueil : Texte des dirigents de l église"
        verbose_name_plural = "Page d'accueil : Texte des dirigents de l église"

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
        verbose_name = "Page d'accueil : Adresse de contact de l eglise"
        verbose_name_plural = "Page d'accueil : Adresse de contact de l eglise"

    
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
        verbose_name = "Page d'accueil : Adresse de contact de l eglise"
        verbose_name_plural = "Page d'accueil : Adresse de contact de l eglise"

class Annonce(models.Model):
    """docstring for Annonce"""
    title = models.CharField(max_length=100)
    def __init__(self, arg):
        super(Annonce, self).__init__()
        self.arg = arg 


def image_post_upload_files(instance, filename):
    filename, file_extension = os.path.splitext(filename)
    return 'POSTS/{0}{1}'.format(instance.slug, file_extension)

class Post(models.Model):
    title = models.CharField('title', max_length=64)
    slug = models.SlugField(max_length=64)
    content = models.TextField('content')
    content_rich = RichTextField(default="")
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    image = models.FileField('Image de l\'nnonce ',upload_to=image_post_upload_files)
    class Meta:
        permissions = (
                    ('view_post', 'Can view post'),
        )
        get_latest_by = 'created_at'
        verbose_name="Eglise Bethnoe : Annonces (espace membres)"
        verbose_name_plural="Eglise Bethnoe : Annonces (espace membres)"

    def __unicode__(self):
        return self.title

        

    @models.permalink
    def get_absolute_url(self):
        return {'post_slug': self.slug}

def logo_upload_files(instance, filename):
    return 'Logo_index_eglisebethnoe/{0}'.format(filename,)

class IndexEgliseBethnoe(models.Model):
    title1 = models.CharField('title du haut a gauche', max_length=64)
    title2 = models.CharField('titre du bas au milieu', max_length=64)
    content = RichTextField()
    video_url = models.URLField('Url de la video de présentation de l\'église' , )
    logo = models.FileField('Logo ',upload_to=logo_upload_files)
    fond_ecran = models.FileField('Fond d ecran', upload_to=logo_upload_files)
    class Meta:
        verbose_name = "Eglise Bethnoe : Video de l'église Bethnoe"
        verbose_name_plural = "Eglise Betnoe : Videos de l'église Bethnoe"


def images_upload_files(instance, filename):
    return 'Evenements_EgliseBethnoe/{0}'.format(filename,)






class ImageEvenement(models.Model):
    image = models.FileField('Photo ',upload_to=images_upload_files)
    titre_image = models.CharField(max_length=128)
    slug = models.SlugField(max_length=150,)
    def __unicode__(self):
        return self.slug  
    def __str__(self):
        return self.slug

class Album(models.Model):
    name = models.CharField(max_length=128)
    slug = models.SlugField(max_length=150,)
    images = models.ManyToManyField(
        ImageEvenement,
        through='PhotoDe',
        through_fields=('album', 'image_evenement'),
    )
    def __unicode__(self):
        return self.slug  
    def __str__(self):
        return self.slug
    class Meta:
        verbose_name = "Eglise Bethnoe : Album pour evenements dans > Eglise Bethnoe > Evenements  "
        verbose_name_plural = "Eglise Bethnoe : Albums pour evenements dans > Eglise Bethnoe > Evenements "





class PhotoDe(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    image_evenement = models.ForeignKey(ImageEvenement, on_delete=models.CASCADE)







class Evenement(models.Model):
    titre = models.CharField(max_length=128)
    content = RichTextField()
    slug = models.SlugField(max_length=150,)
    album =  models.OneToOneField(
        Album,
        on_delete=models.CASCADE,
    )
    TYPES_EVENEMENTS = (
        ('CF', 'Communication fraternelle'),
        ('MR', 'Mariages'),
        ('BE', 'Bâtême d\'eau'),
        ('GD', 'Guérisons et délivrance'),
        )
    type_evenments = models.CharField(max_length=2, choices=TYPES_EVENEMENTS, default='CF')
    def __unicode__(self):
        return self.slug  
    def __str__(self):
        return self.slug
    def first(self):
        return list(self.album.images.all())[0].image
    def images(self):
        return list(self.album.images.all())
    class Meta:
        verbose_name = "Eglise Bethnoe : Evenements "
        verbose_name_plural = "Eglise Bethnoe : Evenements "



class CulteHebdo(models.Model):
    title = models.CharField('Titre Culte Hebdomadaire : ', max_length=64)
    content = RichTextField()
    video_url = models.URLField('Url de la video du culte hebdomadaire' , )
    slug = models.SlugField(max_length=150,)

    class Meta:
        verbose_name="Eglise Bethnoe : Culte hebdomadaire"
        verbose_name_plural="Eglise Bethnoe : Culte hebdomadaire "

def audio_upload_files(instance, filename):
    filename, file_extension = os.path.splitext(filename)
    return 'LOUANGES/{0}{1}'.format(instance.slug, file_extension)





class Audio(models.Model):
    titre = models.CharField("Titre du CD, Titre du fichier",  max_length=250, blank=True)
    audio = models.FileField(upload_to=audio_upload_files)
    slug = models.SlugField(max_length=150,)
    def __unicode__(self):
        return self.slug  
    def __str__(self):
        return self.slug
    class Meta:
        verbose_name="Louange : Fichiers mp3 ou autres ... "
        verbose_name_plural="Louange : Fichiers mp3 ou autres ... "

class CD(models.Model):
    titre = models.CharField("Titre du louange (nom du CD)",max_length=250, blank=True)
    slug = models.SlugField("Slug (Généré automatiquement)",max_length=50,)
    audios = models.ManyToManyField(
        Audio,
        through='AudioDuCD',
        through_fields=('cd', 'audio_cd'),
        related_name="liste",
    )
    def __unicode__(self):
        return self.slug  
    def __str__(self):
        return self.slug
    class Meta:
        verbose_name="Louange : CD à composer "
        verbose_name_plural="Louanges : CDs à composer"




class AudioDuCD(models.Model):
    cd = models.ForeignKey(CD, on_delete=models.CASCADE)
    audio_cd = models.ForeignKey(Audio, on_delete=models.CASCADE)
    Contient = models.ForeignKey(
        Audio,
        on_delete=models.CASCADE,
        related_name="liste_lecture",
    )




def image_priere_upload_files(instance, filename):
    filename, file_extension = os.path.splitext(filename)
    return 'Prieres/{0}{1}'.format(instance.slug, file_extension)

class Priere(models.Model):
    title = models.CharField('title', max_length=64)
    slug = models.SlugField(max_length=64)
    content = RichTextField()   
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    image = models.FileField('Image de l\'nnonce ',upload_to=image_priere_upload_files)
    class Meta:
        permissions = (
                    ('view_post', 'Can view post'),
        )
        get_latest_by = 'created_at'

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = "Eglise Bethnoe : Pririeres (Espace membres) "
        verbose_name_plural = "Eglise Bethnoe :  Pririeres (Espace membres)  "       

class ConfessionDeFoie(models.Model): 
    title = models.CharField('Titre Culte Hebdomadaire : ', max_length=64)
    content = RichTextField()
    logo = models.FileField('Logo ',upload_to=logo_upload_files)
    slug = models.SlugField(max_length=150,)
    class Meta:
        verbose_name = "Eglise Bethnoe : Confession de foie "
        verbose_name_plural = "Eglise Bethnoe :  Confessions de foie "






def image_ecoles_upload_files(instance, filename):
    filename, file_extension = os.path.splitext(filename)
    return 'EcolesDesEnfants/{0}{1}'.format(instance.slug, file_extension)

class Ecoles(models.Model):
    title = models.CharField('title', max_length=64)
    slug = models.SlugField(max_length=64)
    content = RichTextField() 
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    image = models.FileField('Image de l\'nnonce ',upload_to=image_ecoles_upload_files)
    class Meta:
        permissions = (
                    ('view_post', 'Can view post'),
        )
        get_latest_by = 'created_at'

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = "Eglise Bethnoe : Ecole des enfants"
        verbose_name_plural = "Eglise Bethnoe :Ecoles des enfants"






def image_louanges_upload_files(instance, filename):
    filename, file_extension = os.path.splitext(filename)
    return 'Louanges/{0}{1}'.format(instance.slug, file_extension)




class Lien_c(models.Model):
    title = models.CharField('Texte du bouton', max_length=64)
    slug = models.SlugField(max_length=150,)
    url = models.URLField('Url du lien' , )
    def __unicode__(self):
        return self.slug  
    def __str__(self):
        return self.slug
    class Meta:
        verbose_name = "Lien : Lien"
        verbose_name_plural = "Liens : Liens"



class Chapitre_Lien(models.Model):
    title = models.CharField('Titre', max_length=64)
    slug = models.SlugField(max_length=50,)
    content = RichTextField()
    lien = models.ManyToManyField(
        Lien_c,
        through='LienDe',
        through_fields=('chapitre_lien', 'url_p'),
    )
    def __unicode__(self):
        return self.slug  
    def __str__(self):
        return self.slug    
    class Meta:
        verbose_name = "Lien : titre "
        verbose_name_plural = "Liens : titre"

class LienDe(models.Model):
    chapitre_lien = models.ForeignKey(Chapitre_Lien, on_delete=models.CASCADE)
    url_p = models.ForeignKey(Lien_c, on_delete=models.CASCADE)

    lie_a = models.ForeignKey(
        Lien_c,
        on_delete=models.CASCADE,
        related_name="lien_chapitre",
    )




class Contact(models.Model):
    nom = models.CharField(max_length=64)
    prenom = models.CharField(max_length=64)
    email = models.EmailField()
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    telephone = models.CharField(validators=[phone_regex], blank=True,max_length=10)
    description = RichTextField(default="")
    def __unicode__(self):
        return self.nom + " " + self.prenom  
    def __str__(self):
        return self.nom + "  " + self.prenom    
    class Meta:
        verbose_name="Eglise Bethnoe : Message reçu"
        verbose_name_plural="Eglise Bethnoe : Messages reçus"
