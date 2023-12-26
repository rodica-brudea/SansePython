import random
from urllib import request

from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from pyradios import RadioBrowser

import userprofile
from songs.forms import SearchForm
from django.forms import fields
from django.shortcuts import render

# # Create your views here.
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, redirect
#
# # Create your views here.
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView, FormView, DeleteView

from songs.models import MySongs


class SongsView(LoginRequiredMixin, ListView):      # pt user autentificat

    model = MySongs
    template_name = 'songs/song_index.html'


class SearchView(LoginRequiredMixin, FormView):
    template_name = 'songs/rez.html'
    form_class = SearchForm

    def form_valid(self, form):
        self.results = form.get_results()
        return super(SearchView, self).get(self.request)


class CreateSongsView(LoginRequiredMixin, CreateView):

    model = MySongs
    fields = ['comp_path']
    template_name = 'forms.html'

    def get_success_url(self):
        return reverse('supervisor:lista_melodii')


class UpdateSongsView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):

    model = MySongs
    fields = ['comp_path']

    template_name = 'forms.html'

    def get_success_url(self):
        return reverse('songs:song_list')


def myView(request):
    if request.user.username != 'Supervisor':
        queryset = MySongs.objects.all()
        queryset2 = User.objects.all()
        queryset3 = MySongs.mel.through.objects.all()
        get_id = request.user.id
        context = {'music_list': queryset, 'user_list': queryset2, 'mel_list': queryset3, 'usr_id': get_id}
        return render(request, "songs/song_index.html", context)
    else:
        queryset = User.objects.all()
        context = {'user_list': queryset}
        return render(request, 'supervisor/supervisor_index.html', context)


def search(request):
    if request.method == 'GET':
        song = request.GET.get('search_name')
        album = request.GET.get('search_album')
        artist = request.GET.get('search_artist')
        try:
            queryset1 = MySongs.objects.filter(name__icontains=song)
            queryset2 = MySongs.objects.filter(album__icontains=album)
            queryset3 = MySongs.objects.filter(artist__icontains=artist)
            queryset = (queryset1 | queryset2 | queryset3).distinct()
            getsongs = MySongs.mel.through.objects.all()
            get_id = request.user.id
            lista_mel = list(MySongs.mel.through.objects.all())
            query = []

            for i in range(len(lista_mel)):
                for item in queryset:
                    if lista_mel[i].mysongs_id == item.id and lista_mel[i].user_id == get_id:
                        query.append(item)

            a = list(set(queryset))
            b = list(set(query))
            d = [*{*a} - {*b}]
            context = {'music_list': d,
                       'usr_id': get_id,
                       'mel_list': getsongs}

            return render(request,"songs/search.html", context)
        finally:
            pass
    else:
        return render(request,"songs/search.html", {})


# class StergeSongView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
#
#     model = MySongs
#
#     template_name = "songs/sterge_mel.html"
#
#     def test_func(self):
#         if (get_song := MySongs.mel.through.objects.filter(id=self.kwargs['pk'])) and get_song.exists():
#             return True
#         return False
#
#     def get_success_url(self):
#         return reverse("songs:song_index")


def sterge_mel(request):
    rez = request.POST.getlist('legatura')
    leg = int(rez[0])
    MySongs.mel.through.objects.filter(id=leg).delete()
    queryset = MySongs.objects.all()
    queryset2 = User.objects.all()
    queryset3 = MySongs.mel.through.objects.all()
    get_id = request.user.id
    context = {'music_list': queryset, 'user_list': queryset2, 'mel_list': queryset3, 'usr_id': get_id}
    return render(request, "songs/song_index.html", context)


def sterge_final(request):
    if request.user.id:
        usr_id = request.user.id
        MySongs.mel.through.objects.all().filter(id=usr_id).delete()
        utilizator = User(usr_id)
        utilizator.delete()
        return redirect('login')
    return render(request, "registration/login.html", {})


def radio(request, *args):
    indice = random.randrange(250)
    rb = RadioBrowser()
    statii_rock = rb.stations_by_tag('Metal')
    rez = statii_rock[indice]

    # help(RadioBrowser)

    return render(request, "songs/song_index.html", {'url': rez['url'], 'name': rez['name'],
                                                     'country': rez['country'], 'homepage': rez['homepage']})

