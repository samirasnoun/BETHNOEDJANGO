from django.contrib import admin

from models import * 

# Register your models here.
@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'photo')
    search_fields = ('title',)

@admin.register(FondEcran)
class FondEcranAdmin(admin.ModelAdmin):
    list_display = ('title', 'photo', 'afficher', 'caption')
    search_fields = ('title',)

@admin.register(ImageCarrousel)
class ImageCarrousel(admin.ModelAdmin):
    list_display = ('title', 'photo', 'afficher', 'caption')
    search_fields = ('title',)

@admin.register(DirigentEgliseBethnoe)
class DirigentEgliseBethnoe(admin.ModelAdmin):
    list_display = ('nom', 'prenom', 'mail', 'role')

@admin.register(Adresse)
class Adresse(admin.ModelAdmin):
	list_display = ('num_rue', 'type_rue', 'nom_rue', 'code_dep', 'ville' )


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('title', 'slug', 'created_at')
    search_fields = ('title', 'content')
    ordering = ('-created_at',)
    date_hierarchy = 'created_at'

admin.site.register(Post, PostAdmin)

