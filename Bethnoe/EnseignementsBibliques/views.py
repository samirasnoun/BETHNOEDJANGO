# -*- coding: utf8 -*-
from django.shortcuts import render, render_to_response
from django.views.decorators.csrf import csrf_protect
from models import EnseignementBiblique, Auteur, Theme
from django.db.models import Q

# Create your views here.

@csrf_protect 
def EnseignementsBibliques(request):
	enseignementsBibliques = list(EnseignementBiblique.objects.all())
	auteurs = list(Auteur.objects.all())
	themes = list(Theme.objects.all())

	
	return render(request ,'EnseignementsBibliques.html' , { 
		'enseignementsBibliques': enseignementsBibliques,
		'auteurs': auteurs,
		'themes': themes,	
		 } )


@csrf_protect 
def EnseignementsBibliquesDetailView(request, slug):
	enseignementsBibliques = list(EnseignementBiblique.objects.all())

	enseignementBiblique = EnseignementBiblique.objects.get(slug=slug)


	same_auteur_same_theme = list(EnseignementBiblique.objects.filter(auteur = enseignementBiblique.auteur, theme = enseignementBiblique.theme ).exclude(id=enseignementBiblique.id))

	same_theme =  list(EnseignementBiblique.objects.filter(theme  = enseignementBiblique.theme ).exclude(id=enseignementBiblique.id).exclude(auteur = enseignementBiblique.auteur ) )
	same_auteur = list(EnseignementBiblique.objects.filter(auteur = enseignementBiblique.auteur).exclude(id=enseignementBiblique.id).exclude(theme=enseignementBiblique.theme))
	# i = int(same_theme.index(enseignementBiblique))
	# same_theme.pop(i)
	# j= int(same_auteur.index(enseignementBiblique))
	# same_auteur.pop(j)



	print "-------------------"	
	auteurs = list(Auteur.objects.all())
	themes = list(Theme.objects.all())
	
	return render(request ,'EnseignementsBibliques_Video.html' , { 
		'enseignementsBibliques': enseignementsBibliques,
		'ES': enseignementBiblique,
		'auteurs': auteurs,
		'themes': themes,
		'same_auteur': same_auteur,
		'same_theme': same_theme,
		'same_auteur_same_theme': same_auteur_same_theme, 
		
	
		 } )