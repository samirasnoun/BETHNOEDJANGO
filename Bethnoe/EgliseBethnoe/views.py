# -*- coding: utf8 -*-
from django.shortcuts import render, render_to_response, get_object_or_404, get_list_or_404
from django.http import Http404
from django.http import HttpResponse
from EgliseBethnoe.models import *
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponseRedirect
from forms import * 

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
        "accueil": "true",       
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
 


@csrf_protect
def IndexEgliseBethnoePostsDetailView(request, slug):
    post = Post.objects.get(slug=slug)

    index_eglise_bethnoe = list(IndexEgliseBethnoe.objects.all())[0]
    return render(request,
        'index_eglisebethnoe_posts_detail.html', 
        {
        "index_eglise_bethnoe": index_eglise_bethnoe, 
        "post": post, 
        "evenements": "", 

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
def ChapitreLiensView(request):
    index_eglise_bethnoe = list(IndexEgliseBethnoe.objects.all())[0]
    chapite_lien = list(Chapitre_Lien.objects.all())[0]
    liens = list(Lien_c.objects.all())

    return render(request,
        'index_liens.html', 
        {
        "index_eglise_bethnoe": index_eglise_bethnoe,
        "chapite_lien": chapite_lien,  
        "liens": liens,
        } 
        )

@csrf_protect
def AddUser(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)            
            return HttpResponseRedirect('/accounts/login/')
        else:
            render(request, 'registration/adduser.html', {'form': form})


    else:
        form = UserForm() 

    return render(request, 'registration/adduser.html', {'form': form}) 








@csrf_protect
def IndexEgliseBethnoePriereDetailView(request, slug):
    priere = Priere.objects.get(slug=slug); 
    index_eglise_bethnoe = list(IndexEgliseBethnoe.objects.all())[0]
    return render(request,
        'index_eglisebethnoe_prieres_detail.html', 
        {
        "index_eglise_bethnoe": index_eglise_bethnoe, 
        "priere": priere, 
        } 
        )

@csrf_protect
def IndexEgliseBethnoeConfessionFoieView(request):
    
    index_eglise_bethnoe = list(IndexEgliseBethnoe.objects.all())[0]
    confession = list(ConfessionDeFoie.objects.all())[0]
    return render(request,
        'index_eglisebethnoe_prieres_detail.html', 
        {
        "index_eglise_bethnoe": index_eglise_bethnoe, 
        "confession": confession, 
        } 
        )




@csrf_protect
def EcoleDesEnfantsDetailView(request, slug):
    ecole = Ecoles.objects.get(slug=slug); 
    index_eglise_bethnoe = list(IndexEgliseBethnoe.objects.all())[0]
    return render(request,
        'index_eglisebethnoe_ecoledesenfants_detail.html', 
        {
        "index_eglise_bethnoe": index_eglise_bethnoe, 
        "ecole": ecole, 
        } 
        )

@csrf_protect 
def contact(request): 
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cont = Contact(nom=form.cleaned_data['nameField'], prenom=form.cleaned_data['firstNameField'],email = form.cleaned_data['emailField'],telephone = form.cleaned_data['phone_number'], description = form.cleaned_data['descField']  )
            cont.save()
            nom = form.cleaned_data['nameField']
            prenom = form.cleaned_data['firstNameField']
            email = form.cleaned_data['emailField']
            telephone = form.cleaned_data['phone_number']
            description = form.cleaned_data['descField']
            index_eglise_bethnoe = list(IndexEgliseBethnoe.objects.all())[0]
            return render(request,'index_eglisebethnoe.html' , {'prenom': prenom} ) 

            #send_mail('Feedback from your site, topic: %s' % topic,message, sender,['samir.asnoun@gmail.com'])
            #mail_managers(topic + " from " + sender, message, fail_silently=False, connection=None, html_message=None)
            
        else:
            

            return render(request, "index_contact.html", {'form': form })
    else:
        
        form = ContactForm()
        return render(request, "index_contact.html", {'form': form })



@csrf_protect
def EcoleDesEnfantsView(request):
    index_eglise_bethnoe = list(IndexEgliseBethnoe.objects.all())[0]
    ecoles = Ecoles.objects.all()
    return render(request,
        'index_eglisebethnoe_ecoledesenfants.html', 
        {
        "index_eglise_bethnoe": index_eglise_bethnoe, 
        "ecoles": ecoles, 
        } 
        )
