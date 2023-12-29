from django.template.defaulttags import url
from django.urls import path
from songs import views
from songs.views import myView

app_name = 'songs'

urlpatterns = [

    path('', myView, name="my_view"),
    path('search/', views.search, name='search'),
    path('', views.SongsView.as_view(), name="song_list"),
    path('<int:pk>/sterge_mel/', views.sterge_mel, name='sterge_mel'),
    path('sterge_final/', views.sterge_final, name='sterge_final'),
    path('adaugare/', views.CreateSongsView.as_view(), name='adaugare'),
    path('radio/', views.radio, name='radio'),
]
