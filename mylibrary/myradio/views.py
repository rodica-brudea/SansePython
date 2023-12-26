from django.shortcuts import render

# Create your views here.
from pyradios import RadioBrowser
import random


def radio(request, *args):
    indice = random.randrange(50)
    rb = RadioBrowser()
    # statii_rom = rb.stations_by_country('Romania')
    # rez = statii_rom[indice]

    statii_rock = rb.stations_by_tag('Metal')
    rez = statii_rock[indice]

    # help(RadioBrowser)
    # print(rb.countries())

    return render(request, "songs/song_index.html", {'url': rez['url'], 'name': rez['name'],
                                                     'country': rez['country']})
#
#
# # {'url_resolved': rez[0]['url_resolved']})
#
# # radio_final = []
# # for i in lista_radio:
# #     j = i.split('\n')
# #     k = j[0].split('-')
# #     radio_final.append(k[0])
# # nume_fisier = 'myradio/rom.txt'
# # with open(nume_fisier, 'r') as file:
# #     while True:
# #         line = file.readline()
# #         lista_radio.append(line)
# #         if not line:
# #             break
#
# # radio_final = []
#     # for i in lista_radio:
#     #     j = i.split('\n')
#     #     k = j[0].split('-')
#     #     radio_final.append(k[0])
