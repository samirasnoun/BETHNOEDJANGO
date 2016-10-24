# -*- coding: utf8 -*-
from django.shortcuts import render, render_to_response
from django.views.decorators.csrf import csrf_protect
from models import EtudeBiblique, IntrofuctionEtudeBiblique
# Create your views here.






@csrf_protect
def EtudesBibliquesView(request):
	etudesBibliques = list(EtudeBiblique.objects.all())
	intro = list(IntrofuctionEtudeBiblique.objects.all())[0]
	return render(request ,'EtudesBibliques.html' , { 
		'etudesBibliques': etudesBibliques,
		'intro': intro, 
	
		 } )



@csrf_protect
def EtudesBibliquesDetailView(request, slug):
	etude = EtudeBiblique.objects.get(slug=slug)
	intro = list(IntrofuctionEtudeBiblique.objects.all())[0]
	return render(request ,'EtudesBibliquesDetail.html' , { 
		'etude': etude,
		'intro': intro, 
	
		 } )