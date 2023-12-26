from django.shortcuts import render

# Create your views here.

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User

from django.urls import reverse
from django.views.generic import CreateView, ListView, UpdateView

from songs.models import MySongs
from supervisor.forms import NewAccountForm


class CreateNewAccountView(LoginRequiredMixin, CreateView):

    model = User
    template_name = 'forms.html'
    form_class = NewAccountForm

    def get_form_kwargs(self):
        data = super(CreateNewAccountView, self).get_form_kwargs()
        data.update({"pk": None})
        return data

    def get_success_url(self):
        supervisor = User.objects.last()
        supervisor.set_password(supervisor.password)
        supervisor.save()
        return reverse('supervisor:lista_user')


class CreateSongsView(LoginRequiredMixin, CreateView):

    model = MySongs
    template_name = 'forms.html'
    form_class = NewAccountForm


    def get_form_kwargs(self):
        data = super(CreateSongsView, self).get_form_kwargs()
        data.update({"pk": None})
        return data

    def get_success_url(self):
        return reverse('supervisor:lista_melodii')


class ListOfUserView(LoginRequiredMixin, ListView):
    model = User
    template_name = 'supervisor/supervisor_index.html'


class SongsView(LoginRequiredMixin, ListView):      # pt user autentificat

    model = MySongs
    template_name = 'songs/music_index.html'


class UpdateUserView(LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'forms.html'
    form_class = NewAccountForm

    def get_form_kwargs(self):
        data = super(UpdateUserView, self).get_form_kwargs()
        data.update({"pk": self.kwargs['pk']})
        return data

    def get_success_url(self):
        users = User.objects.all().filter(pk=self.kwargs['pk'])
        user = User.objects.get_by_natural_key(users[0])
        user.set_password(user.password)
        user.save()
        return reverse('supervisor:lista_user')


from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from songs.models import MySongs

def sterge_mel(request):

    rez = request.POST.getlist('legatura3')
    leg = int(rez[0])
    MySongs.mel.through.objects.filter(mysongs_id=leg).delete()
    MySongs.objects.filter(id=leg).delete()
    queryset = User.objects.all()
    queyset1 = MySongs.objects.all()
    queryset2 = MySongs.mel.through.objects.all()
    get_id = request.user.id
    context = {'user_list': queryset, 'music_list': queyset1, 'mel_list': queryset2, 'usr_id': get_id}
    return render(request, "supervisor/supervisor_index.html", context)

def sterge_final(request):
    if request.POST.getlist('legatura2'):
        rez = request.POST.getlist('legatura2')
        leg = int(rez[0])
        usr_id = leg
        MySongs.mel.through.objects.all().filter(id=usr_id).delete()
        utilizator = User(usr_id)
        utilizator.delete()
        return redirect('login')
    return render(request, "registration/login.html", {})


