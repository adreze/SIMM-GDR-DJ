from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from GDR.models import User
from .forms import UserForm


def index(request):
    return HttpResponse("Hello, world. You're at the GDR's index.")

def user_list(request):
    users = User.objects.all()
    context = {
        'users': users
    }
    return render(request, 'GDR/users_list.html', context)
