from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User

from django.core.mail import EmailMultiAlternatives
import requests
from django.shortcuts import redirect
from django.template.loader import render_to_string
from django.urls import reverse
from django.views.generic import CreateView, ListView, UpdateView
from django.contrib.auth import get_user
import random
import string

from urllib3.util import request

from songs.models import MySongs
from supervisor.forms import NewAccountForm


class CreateNewAccountView(LoginRequiredMixin, CreateView):

    model = User
    template_name = 'forms.html'
    form_class = NewAccountForm

    # fields = ['first_name', 'last_name', 'password', 'username', 'email']
    # for user in User.objects.all():
    #     if not user.check_password(user.password):
    #         user.set_password(user.password)
    #         user.save()

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

    # fields = ['first_name', 'last_name', 'password', 'username', 'email']
    # for user in User.objects.all():
    #     if not user.check_password(user.password):
    #         user.set_password(user.password)
    #         user.save()

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

