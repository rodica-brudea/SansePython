from django.urls import path

from userprofile import views

app_name = 'userprofile'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('<int:pk1>/<int:pk2>/adauga_melodie/', views.adauga_melodie, name='adauga_melodie'),
]