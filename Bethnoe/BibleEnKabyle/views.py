# -*- coding: utf8 -*-
from django.shortcuts import render, render_to_response, get_object_or_404, get_list_or_404
from django.http import Http404
from django.http import HttpResponse
from EgliseBethnoe.models import FondEcran, ImageCarrousel, DirigentEgliseBethnoe, AdresseSimple, TextDirigentEgliseBethnoe

def BibleEnKabyleView(request):
    return render_to_response('BibleEnKabyle.html' )