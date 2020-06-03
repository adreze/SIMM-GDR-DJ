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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.models import User


urlpatterns = [
    path('', views.index, name='index'),

    path('login', auth_views.LoginView.as_view(), name='login'),
    path('logout', auth_views.LogoutView.as_view(template_name='GDR/registration/logout.html'), name='logout'),
    path('accounts/', include('django.contrib.auth.urls')),

    path('my_replacements', views.my_replacements, name='my_replacements'),
    
    path('add/replacement', views.add_replacement, name='add_replacement'),
    path('add/reinstall', views.add_reinstall, name='add_reinstall'),
    path('add/install', views.add_install, name='add_install'),
    path('add/student_pc', views.add_student_pc, name='add_student_pc'),

    path('edit/<slug:type_p>/<slug:id_p>/', views.edit, name='edit'),
    path('delete/<slug:type_p>/<slug:id_p>/', views.delete, name='delete')
]
