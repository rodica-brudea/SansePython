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
