from __future__ import unicode_literals
from django.db import models
from ckeditor.fields import RichTextField
from django.utils.translation import ugettext as _

class LivreBible(models.Model):
	titre = models.CharField(_("Titre du livre a ajouter"),max_length=250, blank=True)
	ANCIEN_NOUVEAU = (
        ('NV', 'Nouveau Testament'),
        ('AC', 'Ancien Testament'),
        )
	type_na = models.CharField(max_length=2, choices=ANCIEN_NOUVEAU, default='nv')
	def __unicode__(self):
		return self.titre  
	def __str__(self):
		return self.titre  

class ChapitreBible(models.Model):
	content = RichTextField()
	titre = models.CharField(max_length=250, blank=True)
	livre = models.ForeignKey(LivreBible, on_delete=models.CASCADE)
	slug = models.SlugField(max_length=50, default="")

	def __unicode__(self):
		return self.titre  
	def __str__(self):
		return self.titre



