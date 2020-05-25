"""library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.views.generic import TemplateView
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from GDR.views import AboutView


urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('loginin', auth_views.auth_login, name='loginin'),
    path('logout', auth_views.auth_logout, name='logout'),
    path('allusers', views.user_list),
    path('accounts/', include('django.contrib.auth.urls')),
]
