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
from django.shortcuts import redirect

from django import forms


class SongsView(ListView):      # pt user autentificat

    model = MySongs
    template_name = 'songs/song_index.html'


class SearchView(FormView):
    template_name = 'songs/rez.html'
    form_class = SearchForm
    # results = {{ view.results }}

    def form_valid(self, form):
        self.results = form.get_results()
        return super(SearchView, self).get(self.request)

    # def get_success_url(self):
    #     return reverse('songs:song_list')


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

# def myView(request):
#     if request.user.username == 'Supervisor':
#         return redirect('/supervisor/')

def radio(request, *args):
    indice = random.randrange(500)
    rb = RadioBrowser()
    statii_rock = rb.stations_by_tag('Metal')
    rez = statii_rock[indice]

    print(rez['url'])

    # help(RadioBrowser)

    return render(request, "songs/song_index.html", {'url': rez['url'], 'name': rez['name'],
                                                     'country': rez['country']})
def myView(request):
    if request.user.username != 'Supervisor':
        queryset = MySongs.objects.all()
        queryset2 = User.objects.all()
        queryset3 = MySongs.mel.through.objects.all()
        get_id = request.user.id
        context = {'music_list': queryset, 'user_list': queryset2, 'mel_list': queryset3, 'usr_id': get_id}

        # indice = random.randrange(200)
        # rb = RadioBrowser()
        # statii_rock = rb.stations_by_tag('Metal')
        # rez = statii_rock[indice]
        #
        # context['url'] =  rez['url']
        # context['name'] = rez['name']
        # context['country'] =  rez['country']
        return render(request, "songs/song_index.html", context)
    else:
        queryset = User.objects.all()
        context = {'user_list': queryset}
        return render(request, 'supervisor/supervisor_index.html', context)
    # def myView(request):
    # next_url = request.GET.get("next", "supervisor")
    # return redirect(next_url)
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
        return render(request,"songs/search.html",{})

    # c = []
    # for i in a:
    #     k = ""
    #     for j in b:
    #         if i == j:
    #             k = "abc"
    #             break
    #     if k == "":
    #         c.append(i)

#     if request.user.username != 'Supervisor':
#         queryset = MySongs.mel.through.objects.all()
#         get_id = request.user.id
#         context = {'music_list': queryset, 'usr_id': get_id}
#         return render(request, "./song_index.html", context)
#     else:
#         queryset = User.objects.all()
#         context = {'user_list': queryset}
#         return render(request, 'registration/supervisor_index.html', context)
# # # views.py
#
#     return redirect('songs/delete_form/')

# def search(request):
#     form = SearchForm(request.GET)
#     if form.is_valid():
#         query = form.cleaned_data['q']
#     else:
#         query = None
#     return HttpResponse(query)

# def search(request):
#     query = request.GET.get('nume')
#     return HttpResponse(query)
#   # now this one can access id/pk
# def search(request):
#     query = request.GET.get('q')
#     print(query)

# return render(request, 'account/index.html')

# @login_required
# def deactivate_location(request, pk):
#         MySongs.objects.filter(id=pk).update(active=False)
#         return redirect('songs:song_list')
#
#
# @login_required
# def activate_location(request, pk):
#     MySongs.objects.filter(id=pk).update(active=True)
#     return redirect('songs:song_list')
class StergeSongView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):

    model = MySongs

    template_name = "songs/sterge_mel.html"

    def test_func(self):
        if (get_song := MySongs.mel.through.objects.filter(id=self.kwargs['pk'])) and get_song.exists():
            return True
        return False

    def get_success_url(self):
        return reverse("songs:song_index")

    # def sterge_melodie(request):
    #     rez = request.POST.getlist('legatura')
    #     leg = int(rez[0])
    #     MySongs.mel.through.objects.filter(id=leg).delete()
    #
    #     return render(request, "/songs/sterge_mel/", {})
