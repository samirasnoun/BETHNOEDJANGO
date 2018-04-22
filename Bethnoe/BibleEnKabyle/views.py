# -*- coding: utf8 -*-
from django.shortcuts import render, render_to_response, get_object_or_404, get_list_or_404
from django.views.decorators.csrf import csrf_protect
from django.http import Http404
from django.http import HttpResponse
from models import  ChapitreBible , LivreBible
from forms import Recherche
from EnseignementsBibliques.models import Section

livres_avec_chapitres_left, livres_avec_chapitres_right = {}, {}

@csrf_protect
def BibleEnKabyleView(request, ecoute_lecture):
	try:
		section = Section.objects.get(onglet='BLKBL')
	except Section.DoesNotExist:
		section = Section('EBTNE', 'Titre a définir','Contenu vide', 'logo.png') 
	
	text_recherche=""

	if(request.method == 'POST'): 
		form = Recherche(request.POST)
		if form.is_valid():
			text_recherche = form.cleaned_data['text_recherche']
	else :
		form = Recherche()
	
	livs_right = LivreBible.objects.filter(type_na='NV')
	for liv in livs_right :
		#"chap_r = ChapitreBible.objects.filter(livre=liv).filter(titre__contains=text_recherche).filter(content__contains=text_recherche)"
		chap_r = ChapitreBible.objects.filter(livre=liv).filter(content__icontains=text_recherche)
		cc = []
		for c in chap_r:
			cc.append(c)
		livres_avec_chapitres_right[liv] = cc

	livs_left = LivreBible.objects.filter(type_na='AC')
	for liv_l in livs_left : 
		#"chap_l = ChapitreBible.objects.filter(livre=liv_l).filter(titre__contains=text_recherche).filter(content__contains=text_recherche)"
		chap_l = ChapitreBible.objects.filter(livre=liv_l).filter(content__icontains=text_recherche)
		cc_l = []
		for c_l in chap_l:
			cc_l.append(c_l)
		livres_avec_chapitres_left[liv_l] = cc_l

#		if(ecoute_lecture=='lecture'):
#			ecoute_lecture = ''
 
 

	return render(request ,'BibleEnKabyle.html' , { 
		"livres_avec_chapitres_right": livres_avec_chapitres_right, 
		"livres_avec_chapitres_left": livres_avec_chapitres_left, 
		"ecoute_lecture": ecoute_lecture,
		"form": form,
		"section": section,		
		 } )

@csrf_protect
def BibleEnKabyleLectureView(request, slug):
	try:
		section = Section.objects.get(onglet='BLKBL')
	except Section.DoesNotExist:
		section = Section('EBTNE', 'Titre a définir','Contenu vide', 'logo.png') 
	res = ChapitreBible.objects.filter(slug=slug)
	chapitres = []
	for chapi in  res:
		chapitres.append(chapi)

	res_all = ChapitreBible.objects.filter(livre=chapitres[0].livre)
	chapitres_all = []
	for chapi_a in  res_all:
		chapitres_all.append(chapi_a)

	current = chapitres_all.index(chapitres[0])
	prec = ""
	suiv = ""

	if( current > 0 ):
		prec = chapitres_all[current-1]

	if( current+1 < len(chapitres_all) ):
		suiv = chapitres_all[int(current+1)]
 
	return render(request,
		'BibleEnKabyle_lecture.html', 
		{
		"section": section,
		"chapitre": chapitres[0], 
		"chapitres_all": chapitres_all, 
		"current": current, 
		"prec": prec,
		"suiv": suiv, 
		"ecoute_lecture": 'ecoute',

		} 
		)


 
@csrf_protect 
def BibleEnKabyleEcouteView(request, slug):
	chapitre_en_lecture = ChapitreBible.objects.get(slug=slug)
	chapitres = list(ChapitreBible.objects.filter(livre=chapitre_en_lecture.livre))
	current = chapitres.index(chapitre_en_lecture)
	audios = []
	try:
		section = Section.objects.get(onglet='BLKBL')
	except Section.DoesNotExist:
		section = Section('EBTNE', 'Titre a définir','Contenu vide', 'logo.png')
	prec = ""
	suiv = ""
	if( current > 0 ):
		prec = chapitres[current-1]
	if( current+1 < len(chapitres) ):
		suiv = chapitres[int(current+1)]
	return render(request,
		'BibleEnKabyle_ecoute.html', 
		{ "chapitre": chapitre_en_lecture, 
		"chapitres_all": chapitres, 
		"current": current, 
		"prec": prec,
		"suiv": suiv, 
		"ecoute_lecture": 'ecoute',
		"section": section,
		"chapitres": chapitres,

		}

		)




