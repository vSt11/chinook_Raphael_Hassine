from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.views import generic
from django.utils import timezone
from disks.models import Album, Artist, Track

def album_list(request):
    # Récupérer tous les albums de la base de données
    albums = Album.objects.all()
    return render(request, 'album_list.html', {'albums': albums})

def album_detail(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    #tracks = album.track_set.all()
    #artist_name = Album.artist
   # album_title = Album.title
    #album_unitPrice = Album.unitPrice
    
    context = {
        'album' : album
        #'Track': tracks,
        #'Artist.name':artist_name,
        #'Album.title': album_title,
        #'track.unitPrice': album_unitPrice
    }
    
    return render(request, 'album_detail.html', context)