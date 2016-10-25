# -*- coding: utf8 -*-
from django.shortcuts import render, render_to_response
from django.views.decorators.csrf import csrf_protect
from models import EnseignementBiblique, Auteur, Theme
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
	auteurs = list(Auteur.objects.all())
	themes = list(Theme.objects.all())
	
	return render(request ,'EnseignementsBibliques.html' , { 
		'enseignementsBibliques': enseignementsBibliques,
		'auteurs': auteurs,
		'themes': themes,
		
	
		 } )