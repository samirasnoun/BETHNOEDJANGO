# -*- coding: utf8 -*-
from django.shortcuts import render, render_to_response, get_object_or_404, get_list_or_404
from django.http import Http404
from django.http import HttpResponse
from models import  ChapitreBible , LivreBible

livres_avec_chapitres = {}

livres = []
def BibleEnKabyleView(request):
	livs = LivreBible.objects.all()
	for liv in livs :
		print ";;;;;;;;;;;;;;"
		print liv.titre
		chap = ChapitreBible.objects.filter(livre=liv)
		cc = []
		livres.append(liv)
		for c in chap:
			cc.append(c)
			print c.id
		livres_avec_chapitres[liv] = cc

	print "test"
	return render_to_response('BibleEnKabyle.html' , { "livres_avec_chapitres": livres_avec_chapitres, "livres": livres } )