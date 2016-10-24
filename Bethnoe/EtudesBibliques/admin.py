from django.contrib import admin
from models import *  

# Register your models here.
@admin.register(EtudeBiblique)
class ChapitreBibleAdmin(admin.ModelAdmin):
	list_display = (  'titre', 'slug' )
	prepopulated_fields = {"slug": ("titre",)}



@admin.register(IntrofuctionEtudeBiblique)
class ChapitreBibleAdmin(admin.ModelAdmin):
	list_display = (  'titre', 'slug' )
	prepopulated_fields = {"slug": ("titre",)}