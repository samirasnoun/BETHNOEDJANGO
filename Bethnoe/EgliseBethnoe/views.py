# -*- coding: utf8 -*-
from django.shortcuts import render, render_to_response, get_object_or_404, get_list_or_404
from django.http import Http404
from django.http import HttpResponse
from EgliseBethnoe.models import FondEcran, ImageCarrousel, DirigentEgliseBethnoe, AdresseSimple, TextDirigentEgliseBethnoe, IndexEgliseBethnoe

def IndexView(request):
    images_context = []
    try:
        images = FondEcran.objects.all()   
        for m in images:
            images_context.append(m)     
        #chantiers = get_list_or_404(Chantier)
    except Image.DoesNotExist:
        raise Http404

    images_carrousel = []
    try:
        images = ImageCarrousel.objects.all()
        for m in images:
            images_carrousel.append(m)
    except Exception as e:
        raise e

    dirigents_eglise = []
    try:
        dirigeants = DirigentEgliseBethnoe.objects.all()
        for d in dirigeants:
            dirigents_eglise.append(d)
    except Exception as e:
        raise e


    adresses  =[]
    try:
        adress = AdresseSimple.objects.all()       
        for a in adress:
            adresses.append(a)
    except Exception as e:
        raise e

    presentation_equipe_dirigente = []
    try:
        texts = TextDirigentEgliseBethnoe.objects.all()       
        for t in texts:
            presentation_equipe_dirigente.append(t)
    except Exception as e:
        raise e    


    return render_to_response('index.html', 
        {"fond1": images_context[1], 
        "fond2": images_context[0] , 
        "images_carrousel": images_carrousel, 
        "dirigents_eglise": dirigents_eglise, 
        "adresses": adresses[0], 
        "presentation_equipe_dirigente": presentation_equipe_dirigente[0] } )


def IndexEgliseBethnoeView(request):
    index_eglise_bethnoe = list(IndexEgliseBethnoe.objects.all())[0]



    return render_to_response(

        'index_eglisebethnoe.html', 

        {
        "index_eglise_bethnoe": index_eglise_bethnoe, 

        
        } 

        )