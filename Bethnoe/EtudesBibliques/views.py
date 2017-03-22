# -*- coding: utf8 -*-
from django.shortcuts import render, render_to_response
from django.views.decorators.csrf import csrf_protect
from models import EtudeBiblique, IntrofuctionEtudeBiblique
from EnseignementsBibliques.models import *
from django.views.decorators.csrf import csrf_protect
# Create your views here.

@csrf_protect
def EtudesBibliquesView(request):
	etudesBibliques = list(EtudeBiblique.objects.all())
	intro = list(IntrofuctionEtudeBiblique.objects.all())[0]

	try:
		section = Section.objects.get(onglet='ETDBB')
	except Section.DoesNotExist:
		section = Section('EBTNE', 'Titre a définir','Contenu vide', 'logo.png')	

	return render(request ,'EtudesBibliques.html' , { 
		'etudesBibliques': etudesBibliques,
		'intro': intro, 
		'section': section,
	
		 } )



@csrf_protect
def EtudesBibliquesDetailView(request, slug):
	etude = EtudeBiblique.objects.get(slug=slug)
	intro = list(IntrofuctionEtudeBiblique.objects.all())[0]

	try:
		section = Section.objects.get(onglet='ETDBB')
	except Section.DoesNotExist:
		section = Section('EBTNE', 'Titre a définir','Contenu vide', 'logo.png')	 

	return render(request ,'EtudesBibliquesDetail.html' , { 
		'etude': etude,
		'intro': intro, 
		'section': section,
	
		 } )