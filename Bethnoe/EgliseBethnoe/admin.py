from django.contrib import admin

from models import * 

# Register your models here.
# @admin.register(Image)
# class ImageAdmin(admin.ModelAdmin):
#     list_display = ('title', 'photo')
#     search_fields = ('title',)

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

@admin.register(AdresseSimple)
class AdresseSimple(admin.ModelAdmin):
	list_display = ('num_rue', 'type_rue', 'nom_rue', 'code_postale', 'ville' , 'pays')

@admin.register(TextDirigentEgliseBethnoe)
class ClassName(admin.ModelAdmin):
	list_display =('titre','texte')


@admin.register(IndexEgliseBethnoe)
class IndexEgliseBethnoeAdmin(admin.ModelAdmin):
	list_display=('title1', 'title2', 'video_url',)


@admin.register(ImageEvenement)
class ImageEvenement(admin.ModelAdmin):
	list_display=('image',)

class ImagesInline(admin.TabularInline):
    model = Album.images.through

@admin.register(Album)
class Album(admin.ModelAdmin):
	list_display=('name','slug')
	prepopulated_fields = {
    "slug": ("name",)
    }
	inlines = [
        ImagesInline,
    ]






        