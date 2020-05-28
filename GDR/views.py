from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from GDR.models import User
from .forms import UserForm


def index(request):
    return render(request, 'GDR/index.html')


def team_replacements(request):
    return render(request, 'GDR/team_replacements.html')


def my_replacements(request):
    return render(request, 'GDR/my_replacements.html')


def add_replacement(request):
    return render(request, 'GDR/add_replacement.html')


def add_reinstall(request):
    return render(request, 'GDR/add_reinstall.html')


def add_install(request):
    return render(request, 'GDR/add_install.html')


def add_student_pc(request):
    return render(request, 'GDR/add_student_pc.html')



def user_list(request):
    users = User.objects.all()
    context = {
        'users': users
    }
    return render(request, 'GDR/users_list.html', context)
