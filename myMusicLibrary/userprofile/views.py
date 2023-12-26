from django.shortcuts import render

# Create your views here.
from django.contrib.auth import login, authenticate

from django.shortcuts import render, redirect


from userprofile.forms import SignUpForm
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

