"""
URL configuration for mylibrary project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django import views
from songs import views
from django.contrib import admin
from django.contrib.auth.views import LoginView
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('django.contrib.auth.urls'), {'next_page': '/'}, name='login'),
    path('', LoginView.as_view(), name='login'),
    path('songs/', include("songs.urls")),
    path('supervisor/', include("supervisor.urls")),
    path('userprofile/', include("userprofile.urls")),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.MEDIA_URL_1, document_root=settings.MEDIA_ROOT_1)
urlpatterns += static(settings.MEDIA_URL_2, document_root=settings.MEDIA_ROOT_2)
urlpatterns += static(settings.MEDIA_URL_3, document_root=settings.MEDIA_ROOT_3)

