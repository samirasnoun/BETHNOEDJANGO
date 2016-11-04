# -*- coding: utf8 -*-
from django.shortcuts import render, render_to_response, get_object_or_404, get_list_or_404
from django.http import Http404
from django.http import HttpResponse
from EgliseBethnoe.models import *
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect

@csrf_protect
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


    return render(request,'index.html', 
        {"fond1": images_context[1], 
        "fond2": images_context[0] , 
        "images_carrousel": images_carrousel, 
        "dirigents_eglise": dirigents_eglise, 
        "adresses": adresses[0], 
        "presentation_equipe_dirigente": presentation_equipe_dirigente[0] } )

@csrf_protect
def IndexEgliseBethnoeView(request):
    index_eglise_bethnoe = list(IndexEgliseBethnoe.objects.all())[0]
    return render(request,
        'index_eglisebethnoe.html',
        {
        "index_eglise_bethnoe": index_eglise_bethnoe, 
        "evenements": "",         
        } 
        )

@csrf_protect
def IndexEgliseBethnoeEvenementsView(request):
    evenements = list(Evenement.objects.all())
    index_eglise_bethnoe = list(IndexEgliseBethnoe.objects.all())[0]
    return render(request,
        'index_eglisebethnoe_evenments.html', 
        {
        "index_eglise_bethnoe": index_eglise_bethnoe, 
        "evenements": evenements, 
        'type_evenements': Evenement.TYPES_EVENEMENTS
        } 
        )

@csrf_protect
def IndexEgliseBethnoeEvenementsDetailView(request, slug):
    evenement = Evenement.objects.get(slug=slug)
    images = evenement.images
    index_eglise_bethnoe = list(IndexEgliseBethnoe.objects.all())[0]
    return render(request,
        'index_eglisebethnoe_evenments_detail.html', 
        {
        "index_eglise_bethnoe": index_eglise_bethnoe, 
        "evenement": evenement, 
        "evenements": "", 
        'images': images
        } 
        )
 

@login_required(login_url='accounts/login/')
def IndexEgliseBethnoeEspaceMembersView(request):   
    index_eglise_bethnoe = list(IndexEgliseBethnoe.objects.all())[0]
    return render(request,
        'index_eglisebethnoe_espace_members.html', 
        {
        "index_eglise_bethnoe": index_eglise_bethnoe, 
        } 
        )

@csrf_protect 
def IndexForumView(request):   
    index_eglise_bethnoe = list(IndexEgliseBethnoe.objects.all())[0]
    return render(request,
        'index_forum.html', 
        {
        "index_eglise_bethnoe": index_eglise_bethnoe, 
        } 
        )

@csrf_protect
def LouangesView(request):
    index_eglise_bethnoe = list(IndexEgliseBethnoe.objects.all())[0]
    cds = list(CD.objects.all())
    return render(request,
        'index_louanges.html', 
        {
        "index_eglise_bethnoe": index_eglise_bethnoe, 
        "cds": cds,
        } 
        )

@csrf_protect
def LouangesLectureView(request, slug):
    cd = CD.objects.get(slug=slug)
    audios = list(cd.audios.all())

    print type(cd)
    print "!!!!!!!!!!!!!"
    print type(audios)
    return render(request,
        'index_louanges_lecture.html',
        {
        "cd": cd,
        "audios": audios,
        }
        )


@csrf_protect
def PostsView(request):
    index_eglise_bethnoe = list(IndexEgliseBethnoe.objects.all())[0]
    posts = list(Post.objects.all())
    return render(request,
        'index_posts.html', 
        {
        "index_eglise_bethnoe": index_eglise_bethnoe, 
        "posts": posts,
        } 
        )



@csrf_protect
def PrieresView(request):
    index_eglise_bethnoe = list(IndexEgliseBethnoe.objects.all())[0]
    prieres = list(Priere.objects.all())
    return render(request,
        'index_prieres.html', 
        {
        "index_eglise_bethnoe": index_eglise_bethnoe, 
        "prieres": prieres,
        } 
        )



@csrf_protect
def ConfessionFoieView(request):
    index_eglise_bethnoe = list(IndexEgliseBethnoe.objects.all())[0]
    prieres = list(Priere.objects.all())
    return render(request,
        'index_prieres.html', 
        {
        "index_eglise_bethnoe": index_eglise_bethnoe, 
        "prieres": prieres,
        } 
        )