# Create your views here.
# -*- coding: utf8 -*-
from django.shortcuts import render, render_to_response, get_object_or_404, get_list_or_404
from django.http import Http404
from django.http import HttpResponse
from EgliseBethnoe.models import ImageAccueil, ImageBackgroud



  

# Create your views here.

#Mosaique Projets
def IndexView(request):
    images_context = []
    try:
        images = ImageAccueil.objects.all()
        #chantiers = get_list_or_404(Chantier)
    except ImageAccueil.DoesNotExist:
        raise Http404
    
    for im in images:                
        if (im.afficher == 'oui' and im not in images):
            images_context.append(im)
    try:
    	background = ImageBackgroud.objects.all()
    except ImageBackgroud.DoesNotExist:
    	raise Http404

    return render_to_response('index.html', {"images": images, "background": background} )