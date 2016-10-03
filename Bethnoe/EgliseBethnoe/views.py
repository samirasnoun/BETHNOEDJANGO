# -*- coding: utf8 -*-
from django.shortcuts import render, render_to_response, get_object_or_404, get_list_or_404
from django.http import Http404
from django.http import HttpResponse
from EgliseBethnoe.models import FondEcran, ImageCarrousel,DirigentEgliseBethnoe

def IndexView(request):
    images_context = []
    try:
        images = FondEcran.objects.all()        
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
        print dirigeants
        for d in dirigeants:
            dirigents_eglise.append(d)
    except Exception as e:
        raise e

    return render_to_response('index.html', {"image": images[0], "images_carrousel": images_carrousel, "dirigents_eglise": dirigents_eglise} )