from __future__ import unicode_literals

from django.db import models

# Create your models here.

from django.db import models
from ckeditor.fields import RichTextField

class Post(models.Model):
    content = RichTextField()



class ChapitreBible(models.Model):
	content = RichTextField()

