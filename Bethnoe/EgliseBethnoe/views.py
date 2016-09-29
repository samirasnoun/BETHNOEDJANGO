# -*- coding: utf8 -*-
from django.shortcuts import render, render_to_response, get_object_or_404, get_list_or_404
from django.http import Http404
from django.http import HttpResponse
from EgliseBethnoe.models import Image

def IndexView(request):
    images_context = []
    try:
        images = Image.objects.all()
        #chantiers = get_list_or_404(Chantier)
    except Image.DoesNotExist:
        raise Http404
    return render_to_response('index.html', {"image": images[0],} )