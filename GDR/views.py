from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from GDR.models import User
from .forms import UserForm


@login_required
def index(request):
    return render(request, 'GDR/index.html')


# def login(request):
#     username = request.POST['username']
#     password = request.POST['password']
#     user = authenticate(request, username=username, password=password)
#     if user is not None:
#         login(request, user)
#         # Redirect to a success page.
#         ...
#     else:
#         # Return an 'invalid login' error message.
#         ...


@login_required
def team_replacements(request):
    return render(request, 'GDR/team_replacements.html')


@login_required
def my_replacements(request):
    return render(request, 'GDR/my_replacements.html')


@login_required
def add_replacement(request):
    return render(request, 'GDR/add_replacement.html')


@login_required
def add_reinstall(request):
    return render(request, 'GDR/add_reinstall.html')


@login_required
def add_install(request):
    return render(request, 'GDR/add_install.html')


@login_required
def add_student_pc(request):
    return render(request, 'GDR/add_student_pc.html')


def user_list(request):
    users = User.objects.all()
    context = {
        'users': users
    }
    return render(request, 'GDR/users_list.html', context)
