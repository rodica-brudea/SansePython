from django.urls import path

from userprofile import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('adauga_melodie/', views.adauga_melodie, name='add'),
]