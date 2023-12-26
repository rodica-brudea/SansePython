from django.template.defaulttags import url
from django.urls import path
from songs import views, views2
from songs.views import myView

app_name = 'songs'

urlpatterns = [

    path('', myView),
    path('search/', views.search, name='search'),
    path('', views.SongsView.as_view(), name="song_list"),
    path('sterge_mel.html', views2.sterge_mel, name='sterge_mel'),
    path('sterge_final/', views2.sterge_final, name='sterge_final'),
    path('adaugare/', views.CreateSongsView.as_view(), name='adaugare'),
    path('cautare/', views.SearchView.as_view(), name='cautare'),
    path('radio/', views2.radio, name='radio'),
    path('<int:pk>/modificare/', views.UpdateSongsView.as_view(), name='modificare'),
    # path('<int:pk>/sterge/', views.StergeSongView.as_view(), name='sterge'),



    # path('<int:pk>/dezactiveaza/', views.deactivate_location, name='dezactiveaza'),
    # path('<int:pk>/activeaza/', views.activate_location, name='activeaza'),
]
