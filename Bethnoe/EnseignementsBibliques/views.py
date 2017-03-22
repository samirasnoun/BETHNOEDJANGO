# -*- coding: utf8 -*-
from django.shortcuts import render, render_to_response
from django.views.decorators.csrf import csrf_protect
from models import EnseignementBiblique, Auteur, Theme, Section, EglisePartenaire
from django.db.models import Q

@csrf_protect 
def EnseignementsBibliques(request):
	enseignementsBibliques = list(EnseignementBiblique.objects.all())
	auteurs = list(Auteur.objects.all())
	themes = list(Theme.objects.all())
	
	try:
		section = Section.objects.get(onglet='ENSBI')
	except Section.DoesNotExist:
		section = Section('EBTNE', 'Titre a définir','Contenu vide', 'logo.png')	
	
	return render(request ,'EnseignementsBibliques.html' , { 
		'enseignementsBibliques': enseignementsBibliques,
		'auteurs': auteurs,
		'themes': themes,
		'section': section,	
		 } )

@csrf_protect 
def EnseignementsBibliquesDetailView(request, slug):
	enseignementsBibliques = list(EnseignementBiblique.objects.all())
	enseignementBiblique = EnseignementBiblique.objects.get(slug=slug)
	same_auteur_same_theme = list(EnseignementBiblique.objects.filter(auteur = enseignementBiblique.auteur, theme = enseignementBiblique.theme ).exclude(id=enseignementBiblique.id))
	same_theme =  list(EnseignementBiblique.objects.filter(theme  = enseignementBiblique.theme ).exclude(id=enseignementBiblique.id).exclude(auteur = enseignementBiblique.auteur ) )
	same_auteur = list(EnseignementBiblique.objects.filter(auteur = enseignementBiblique.auteur).exclude(id=enseignementBiblique.id).exclude(theme=enseignementBiblique.theme))
	auteurs = list(Auteur.objects.all())
	themes = list(Theme.objects.all())
	
	try:
		section = Section.objects.get(onglet='ENSBI')
	except Section.DoesNotExist:
		section = Section('EBTNE', 'Titre a définir','Contenu vide', 'logo.png')
	
	return render(request ,'EnseignementsBibliques_Video.html' , { 
		'section': section,
		'enseignementsBibliques': enseignementsBibliques,
		'ES': enseignementBiblique,
		'auteurs': auteurs,
		'themes': themes,
		'same_auteur': same_auteur,
		'same_theme': same_theme,
		'same_auteur_same_theme': same_auteur_same_theme, 	
		 } )

@csrf_protect 
def EglisesPartenairesView(request):
	eglisePartenaires = list(EglisePartenaire.objects.all())
	
	try:
		section = Section.objects.get(onglet='EGPTR')
	except Section.DoesNotExist:
		section = Section('EBTNE', 'Titre a définir','Contenu vide', 'logo.png')

	return render(request ,'EglisesPartenaires.html' , { 
		'eglisePartenaires': eglisePartenaires,
		'section': section, 
		 } )

@csrf_protect 
def EglisesPartenairesDetailView(request, slug):
	eglise = EglisePartenaire.objects.get(slug=slug)
	section = Section.objects.get
	try:
		section = Section.objects.get(onglet='EGPTR')
	except Section.DoesNotExist:
		section = Section('EBTNE', 'Titre a définir','Contenu vide', 'logo.png')
	
	return render(request ,'EglisesPartenaires_Video.html' , { 
		'eglise': eglise,
		'section': section, 
	
		 } )