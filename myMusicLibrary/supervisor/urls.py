from django.contrib.auth import views
from django.urls import path

from songs import views
from supervisor import views

app_name = 'supervisor'

urlpatterns = [
    path('', views.ListOfUserView.as_view(), name="lista_user"),
    path('lista_melodii/', views.SongsView.as_view(), name="lista_melodii"),
    path('adaugare/', views.CreateNewAccountView.as_view(), name='adaugare'),
    path('<int:pk>/adauga_melodii/', views.CreateSongsView.as_view(), name='adauga_melodii'),
    path('<int:pk>/modificare/', views.UpdateUserView.as_view(), name='modificare'),
    path('views1/sterge_mel/', views.sterge_mel, name='sterge_mel'),
    path('sterge_final/', views.sterge_final, name='sterge_final'),
]