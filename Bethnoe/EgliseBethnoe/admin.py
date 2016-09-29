from django.contrib import admin
from django.contrib.admin.sites import AdminSite
from models import *

# Register your models here.
@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'photo')
    search_fields = ('title',)


@admin.register(FondEcran)
class FondEcranAdmin(admin.ModelAdmin):
    list_display = ('title', 'photo')
    search_fields = ('title',)

    



class AdminEgliseBethnoe(AdminSite):
	site_header = 'Site de Bethnoe'
	site_title = 'Eglise Bethnoe' 
	index_title = 'Eglise Bethnoe'


class FondEcranAdmin(admin.ModelAdmin):
    list_display = ('title', 'photo')
    search_fields = ('title',)


adminEgliseBethnoe = AdminEgliseBethnoe(name='adminEB')

adminEgliseBethnoe.register(FondEcran, FondEcranAdmin)
adminEgliseBethnoe.register(Annonce)
