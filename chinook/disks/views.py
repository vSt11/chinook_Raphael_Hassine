from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from disks.models import Album

def album_list(request):
    # Récupérer tous les albums de la base de données
    albums = Album.objects.all()
    return render(request, 'album_list.html', {'albums': albums})

def album_detail(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    tracks = album.track_set.all()
    artist_name = album.artist.name
    album_title = album.title
    album_price = album.price
    context = {
        'tracks': tracks,
        'artist_name': artist_name,
        'album_title': album_title,
        'album_price': album_price
    }
    return render(request, 'disks/album_detail.html', context)
