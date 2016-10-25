# -*- coding: utf8 -*-
from django.shortcuts import render, render_to_response
from django.views.decorators.csrf import csrf_protect
from models import EnseignementBiblique
# Create your views here.






@csrf_protect
def EnseignementsBibliques(request):
	enseignementsBibliques = list(EnseignementBiblique.objects.all())
	
	return render(request ,'EnseignementsBibliques.html' , { 
		'enseignementsBibliques': enseignementsBibliques,
		
	
		 } )