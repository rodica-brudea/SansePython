from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import request
import requests
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import CreateView

from userprofile.forms import SignUpForm
from django.contrib.auth.models import User
from songs.models import MySongs


from songs.models import MySongs

def signup(request):
        if request.method == 'POST':
            form = SignUpForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                raw_password = form.cleaned_data.get('password1')
                user = authenticate(username=username, password=raw_password)
                login(request, user)
                return render(request, 'songs/song_index.html', {'form': form})
        else:
            form = SignUpForm()
        return render(request, 'registration/signup.html', {'form': form})



def adauga_melodie(request):

    rez = request.POST.getlist('melodie')
    muz_id = int(rez[0])
    rez2 = request.POST.getlist('utiliz')
    urs_id = int(rez2[0])


    through_instance = MySongs.mel.through.objects.latest('id')
    latest_mel_user = through_instance.user
    latest_mel_mysongs = through_instance.mysongs
    nr = through_instance.id
    numar = len(MySongs.mel.through.objects.all())

    addsongs = MySongs.mel.through.objects.create(pk=nr + 1, mysongs_id=muz_id, user_id=urs_id)
    addsongs.save()


    return redirect('songs:song_list')

# def functie(request):
#     usr_id = request.user.id
#     if request.method == 'GET':
#         mel_id = request.GET.get('search_mel_id')
#         try:
#             queryset1 = MySongs.objects.filter(name__icontains=song)
#             queryset2 = MySongs.objects.filter(album__icontains=album)
#             queryset3 = MySongs.objects.filter(artist__icontains=artist)
#             queryset = (queryset1 | queryset2 | queryset3).distinct()
#             getsongs = MySongs.mel.through.objects.all()
#
#             get_id = request.user.id
#             context = {'music_list': queryset,
#                        'usr_id': get_id,
#                        'mel_id': getsongs}
#             # filter returns a list so you might consider skip except part
#             return render(request,"songs/search.html", context)
#         finally:
#             pass
#     else:
#         return render(request,"songs/search.html",{})

