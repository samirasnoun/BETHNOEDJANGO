# -*- coding: utf8 -*-
from django.shortcuts import render, render_to_response, get_object_or_404, get_list_or_404
from django.http import Http404
from django.http import HttpResponse
from models import  ChapitreBible , LivreBible

livres_avec_chapitres_left, livres_avec_chapitres_right = {}, {}

def BibleEnKabyleView(request):
	livs_right = LivreBible.objects.filter(type_na='NV')
	for liv in livs_right :
		print "right :" + liv.titre
		chap_r = ChapitreBible.objects.filter(livre=liv)
		cc = []
		for c in chap_r:
			cc.append(c)
		livres_avec_chapitres_right[liv] = cc

	livs_left = LivreBible.objects.filter(type_na='AC')
	for liv_l in livs_left :
		print "left :" + liv_l.titre
		chap_l = ChapitreBible.objects.filter(livre=liv_l)
		cc_l = []
		for c_l in chap_l:
			cc_l.append(c_l)
		livres_avec_chapitres_left[liv_l] = cc_l

	return render_to_response('BibleEnKabyle.html' , { 
		"livres_avec_chapitres_right": livres_avec_chapitres_right, 
		"livres_avec_chapitres_left": livres_avec_chapitres_left, 
		 } )

def BibleEnKabyleLectureView(request, slug):
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

	return render_to_response(
		'BibleEnKabyle_lecture.html', 
		{"chapitre": chapitres[0], 
		"chapitres_all": chapitres_all, 
		"current": current, 
		"prec": prec,
		"suiv": suiv, } 
		)



def BibleEnKabyleEcouteView(request, slug):

	return render_to_response(
		'BibleEnKabyle_ecoute.html', 

		)



	