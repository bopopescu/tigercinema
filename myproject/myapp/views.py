9
# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
from django.conf import settings
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from myproject.myapp.models import Document
from myproject.myapp.forms import DocumentForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import imageio
imageio.plugins.ffmpeg.download()
from moviepy.editor import *
import os
import functools
import operator
from django.contrib.contenttypes.fields import GenericRelation
from star_ratings.models import Rating
from urllib.request import urlopen

movie_count=1

@login_required(login_url='/accounts/login/',redirect_field_name='/myapp/homepage/')
def homepage(request):
    user=request.user
    netid=user.username
    # Load documents for the list page
    documents = Document.objects.all()
    rateddocuments = Document.objects.filter(ratings__isnull=False).order_by('ratings__average').reverse()[0:4]

    # Render list page with the documents and the form
    return render(
        request,
        'myapp/homepage.html',
        {'documents': documents, 'rateddocuments': rateddocuments, 'netid':netid}
    )

@login_required(login_url='/accounts/login/',redirect_field_name='/myapp/homepage/')
def feedback(request):
    user=request.user
    netid=user.username
    return render(request,'myapp/feedback.html',{'netid':netid})


def welcome(request):
    return render(request, 'myapp/welcome.html')


@login_required(login_url='/accounts/login/',redirect_field_name='/myapp/homepage/')
def uploadform(request):
    user=request.user
    netid=user.username
    global movie_count
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            user=request.user
            movie_count+=1
            firstname = form.cleaned_data['fname']
            lastname = form.cleaned_data['lname']
            descript = form.cleaned_data['description']
            titlename = form.cleaned_data['title']
            choiceval = form.cleaned_data['choice']
            url = form.cleaned_data['docfile']
            thumb = form.cleaned_data['thumbnail']
            punetid = user.username
            newdoc = Document(fname = firstname, lname = lastname, title = titlename, 
                              thumbnail = thumb, description = descript, 
                              choice = choiceval, docfile=url, netid = punetid)

            newdoc.save()
            # Redirect to the document list after POST
            return HttpResponseRedirect('/myapp/homepage/')
    else:
        form = DocumentForm()  # A empty, unbound form

        # Load documents for the list page
        #documents = Document.objects.all()

    return render(
        request, 'myapp/uploadform.html',
        { 'form':form, 'netid':netid}
        )

@login_required(login_url='/accounts/login/',redirect_field_name='/myapp/homepage/')
def documentary(request):
 # Load documents for the list page
    documents = Document.objects.filter(choice__exact='2')
    user=request.user
    netid=user.username

    # Render list page with the documents and the form
    return render(
        request,
        'myapp/documentary.html',
        {'documents': documents,'netid':netid}
    )

@login_required(login_url='/accounts/login/',redirect_field_name='/myapp/homepage/')
def narrative(request):
 # Load documents for the list page
    documents = Document.objects.filter(choice__exact='1')
    user=request.user
    netid=user.username

    # Render list page with the documents and the form
    return render(
        request,
        'myapp/narrative.html',
        {'documents': documents,'netid':netid}
    )


# http://stackoverflow.com/questions/20205137/how-to-delete-files-in-django
@login_required(login_url='/accounts/login/',redirect_field_name='/myapp/homepage/')
def delete(request):
    global movie_count
    if request.method != 'POST':
        raise Http404
    docId = request.POST.get('docfile', None)
    documents = Document.objects.all()
    lastDocument = documents[]
    docToDel = get_object_or_404(Document, pk = docId)
    #docToDel.docfile.delete()
    docToDel.delete()
    movie_count -= 1
    newdoc = Document(fname = lastDocument.fname, lname = lastDocument.lname, title = lastDocument.title, 
                              thumbnail = lastDocument.thumb, description = lastDocument.description, 
                              choice = lastDocument.choice, docfile=lastDocument.docfile, netid = lastDocument.netid,pk = docToDel.pk)
    newdoc.save()
    lastDocument.delete()
    return HttpResponseRedirect('/myapp/homepage/')

@login_required(login_url='/accounts/login/',redirect_field_name='/myapp/homepage/')
def search(request):

    if request.method == 'GET':
        user=request.user
        netid=user.username
        query = request.GET.get('search', None)
        if query:
            query_list = query.split()
            documents = Document.objects.filter(
                functools.reduce(operator.or_, 
                                (Q(fname__icontains=q) for q in query_list)) |
                functools.reduce(operator.or_, 
                                (Q(lname__icontains=q) for q in query_list)) |
                functools.reduce(operator.or_, 
                                (Q(title__icontains=q) for q in query_list))
                )
            return render(
                    request,
                    'myapp/searchlistings.html',
                    {'documents': documents,'netid':netid}
            )
        else: return HttpResponseRedirect('/myapp/homepage/')

@login_required(login_url='/accounts/login/',redirect_field_name='/myapp/homepage/')
def play(request, user_id):
    documents = Document.objects.all()
    user=request.user
    netid=user.username
    paginator = Paginator(documents, 1) # Show 1 video per page
    page = int(user_id) - documents[0].position + 1
    rateddocuments = Document.objects.filter(ratings__isnull=False).order_by('ratings__average').reverse()[0:4]
    try:
        video = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        video= paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        video= paginator.page(paginator.num_pages)


    return render(request, 'myapp/play.html', {'video': video, 'rateddocuments':rateddocuments, 'netid':netid})


@login_required(login_url='/accounts/login/',redirect_field_name='/myapp/homepage/')
def mymovies(request):
    user=request.user
    netid=user.username
    documents = Document.objects.filter(netid=netid)
    return render(request, 'myapp/mymovies.html', {'documents': documents,'netid':netid})




