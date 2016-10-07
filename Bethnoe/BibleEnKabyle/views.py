# -*- coding: utf8 -*-
from django.shortcuts import render, render_to_response, get_object_or_404, get_list_or_404
from django.http import Http404
from django.http import HttpResponse
from models import  ChapitreBible , LivreBible, Chapitre , Livre

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

