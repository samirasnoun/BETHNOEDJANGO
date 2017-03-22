from django.contrib import admin 
from models import *  

class AuteurInline(admin.TabularInline):
    model = Auteur   

class ThemeInline(admin.TabularInline):
    model = Theme 

@admin.register(EnseignementBiblique)
class EnseignementBibliqueAdmin(admin.ModelAdmin):
	list_display = ('titre','type_media', 'auteur', 'theme', 'media')
	prepopulated_fields = {"slug": ("titre",)}


@admin.register(Auteur)
class AuteurAdmin(admin.ModelAdmin):
	list_display = ('nom','prenom', 'slug',)
	prepopulated_fields = {"slug": ("nom","prenom")}


@admin.register(Theme)
class ThemeAdmin(admin.ModelAdmin):
	list_display = ('titre', 'slug',)
	prepopulated_fields = {"slug": ("titre",)}


@admin.register(Section)
class ThemeAdmin(admin.ModelAdmin):
	list_display = ('titre', 'content', 'media')

@admin.register(EglisePartenaire)
class EglisePartenaireAdmin(admin.ModelAdmin):
	list_display = ('titre', 'slug', 'media', 'content')
	prepopulated_fields = {"slug": ("titre",)}


