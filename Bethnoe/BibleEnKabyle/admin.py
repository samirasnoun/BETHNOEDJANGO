from django.contrib import admin 
from models import * 

class ChapitreBibleInline(admin.TabularInline):
    model = ChapitreBible   

@admin.register(LivreBible)
class LivreBibleAdmin(admin.ModelAdmin):
	list_display = ('type_na' ,'titre',)

@admin.register(ChapitreBible)
class ChapitreBibleAdmin(admin.ModelAdmin):
	list_display = ( 'livre', 'titre' )

# @admin.register(Livre)
# class LivreBibleAdmin(admin.ModelAdmin):
# 	list_display = ('type_na' , 'titre', )

# @admin.register(Chapitre)
# class ChapitreBibleAdmin(admin.ModelAdmin):
# 	list_display = (  'titre' , )