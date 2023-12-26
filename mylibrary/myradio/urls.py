from django.urls import path

from myradio import views

app_name = 'myradio'

urlpatterns = [
    path('radio/', views.radio, name='radio'),
]