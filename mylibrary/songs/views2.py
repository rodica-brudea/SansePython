from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from songs.models import MySongs

from django.shortcuts import render

# Create your views here.
from pyradios import RadioBrowser
import random


def sterge_mel(request):

    rez = request.POST.getlist('legatura')
    leg = int(rez[0])
    MySongs.mel.through.objects.filter(id=leg).delete()
    # if request.user.username != 'Supervisor':
    queryset = MySongs.objects.all()
    queryset2 = User.objects.all()
    queryset3 = MySongs.mel.through.objects.all()
    get_id = request.user.id
    context = {'music_list': queryset, 'user_list': queryset2, 'mel_list': queryset3, 'usr_id': get_id}
    return render(request, "songs/song_index.html", context)
    # else:
    #     queryset = User.objects.all()
    #     queryset1 = MySongs.objects.all()
    #     queryset2 = MySongs.mel.through.objects.all()
    #     get_id = request.user.id
    #     context = {'user_list': queryset, 'song_list': queryset1, 'mel_list': queryset2, 'usr_id': get_id}
    #     return render(request, 'supervisor/supervisor_index.html', context)

def sterge_final(request):
    if request.user.id:
        usr_id = request.user.id
        MySongs.mel.through.objects.all().filter(id=usr_id).delete()
        utilizator = User(usr_id)
        utilizator.delete()
        return redirect('login')
    return render(request, "registration/login.html", {})


def radio(request, *args):
    indice = random.randrange(200)
    rb = RadioBrowser()
    statii_rock = rb.stations_by_tag('Metal')
    rez = statii_rock[indice]

    print(rez['url'])

    # help(RadioBrowser)

    return render(request, "songs/song_index.html", {'url': rez['url'], 'name': rez['name'],
                                                     'country': rez['country']})

