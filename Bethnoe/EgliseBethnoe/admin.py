from django.contrib import admin

from models import *  

# Register your models here.
# @admin.register(Image)
# class ImageAdmin(admin.ModelAdmin):
#     list_display = ('title', 'photo')
#     search_fields = ('title',)


#@admin.register(Image)
#class ImageAdmin(admin.ModelAdmin):
#    list_display=('title','photo',)

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
    list_display = ('nom',  'role')


@admin.register(AdresseSimple)
class AdresseSimple(admin.ModelAdmin):
	list_display = ('num_rue', 'type_rue', 'nom_rue', 'code_postale', 'ville' , 'pays')

@admin.register(TextDirigentEgliseBethnoe)
class ClassName(admin.ModelAdmin):
	list_display =('titre','texte')


@admin.register(IndexEgliseBethnoe)
class IndexEgliseBethnoeAdmin(admin.ModelAdmin):
	list_display=('title1', 'title2', 'video_url',)


#@admin.register(ImageEvenement)
#class ImageEvenement(admin.ModelAdmin):
#	list_display=('id','image','titre_image','slug')
#	prepopulated_fields = {
#    "slug": ("titre_image",)
#    }

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

@admin.register(Evenement)
class Evenement(admin.ModelAdmin):
    list_display = ('titre','album')
    prepopulated_fields = {
    "slug": ("titre",)
    }


@admin.register(CulteHebdo)
class CulteHebdo(admin.ModelAdmin):
    list_display=('title','slug', 'video_url')
    prepopulated_fields = {
    "slug": ("title",)
    }

@admin.register(Audio)
class AudioAdmin(admin.ModelAdmin):
    list_display=('titre','audio','slug',)
    prepopulated_fields = {
    "slug": ("titre",)
    }

class AudioInline(admin.TabularInline):
    model = CD.audios.through

@admin.register(CD)
class CDAdmin(admin.ModelAdmin):
    list_display=('titre','slug')
    prepopulated_fields = {
    
    "slug": ("titre",), 

    }
    
    inlines = [
        AudioInline,
    ]


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display=('title', 'slug','image',)
    prepopulated_fields = {
    
    "slug": ("title",), 

    }

@admin.register(Priere)
class PriereAdmin(admin.ModelAdmin):
    list_display=('title', 'slug','image',)
    prepopulated_fields = {
    
    "slug": ("title",), 

    }


@admin.register(Ecoles)
class PriereAdmin(admin.ModelAdmin):
    list_display=('title', 'slug','image',)
    prepopulated_fields = {
    
    "slug": ("title",), 

    }


@admin.register(ConfessionDeFoie)
class PriereAdmin(admin.ModelAdmin):
    list_display=('title', 'slug','logo',)
    prepopulated_fields = {
    
    "slug": ("title",), 

    }


@admin.register(Lien_c)
class LienAdmin(admin.ModelAdmin):
    list_display=('title','slug', 'url')
    prepopulated_fields = {
    "slug": ("title",)
    }

class LienInline(admin.TabularInline):
    model = Chapitre_Lien.lien.through


@admin.register(Chapitre_Lien)
class ChapitreLienAdmin(admin.ModelAdmin):
    list_display=('title','slug')
    prepopulated_fields = {    
    "slug": ("title",), 
    }
    inlines = [
        LienInline,
    ]



@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display=('nom','prenom', 'email','telephone')
