from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect

from GDR.forms import PcStudentsForm, InstallForm
from GDR.models import Install, StudentPC, Replacement, Reinstall


#from .forms import UserForm


@login_required
def index(request):
    current_team = "Aucune"
    current_team_ABV = "Aucune"

    if request.user.groups.filter(name="SIMM-Centre").exists():
        current_team = "SIMM-Centre"
        current_team_ABV = "CE"
    if request.user.groups.filter(name="SIMM-Mercier").exists():
        current_team = "SIMM-Mercier"
        current_team_ABV = "ME"

    if request.user.groups.filter(name="SIMM-MO").exists():
        current_team = "SIMM-MO"
        current_team_ABV = "MO"

    #Install.objects.filter(id=1).delete()
    #if the order_by doesn't work try -dateplanned
    installs = Install.objects.filter(byteam=current_team_ABV).order_by('dateplanned')
    reinstalls = Reinstall.objects.filter(byteam=current_team_ABV).order_by('dateplanned')
    replacements = Replacement.objects.filter(byteam=current_team_ABV).order_by('dateplanned')
    student_pcs = StudentPC.objects.filter(byteam=current_team_ABV).order_by('dateplanned')
    #all_replacement = [installs, reinstalls, replacements, student_pcs]
    context = {
        'installs': installs,
        'reinstalls': reinstalls,
        'replacements': replacements,
        'student_pcs': student_pcs,
        'current_team': current_team
        #'all_replacement': all_replacement
    }
    return render(request, 'GDR/index.html', context)


@login_required
def my_replacements(request):
    installs = Install.objects.filter(simmuser=request.user).order_by('dateplanned')
    reinstalls = Reinstall.objects.filter(simmuser=request.user).order_by('dateplanned')
    replacements = Replacement.objects.filter(simmuser=request.user).order_by('dateplanned')
    student_pcs = StudentPC.objects.filter(simmuser=request.user).order_by('dateplanned')
    #all_replacement = [installs, reinstalls, replacements, student_pcs]
    context = {
        'installs': installs,
        'reinstalls': reinstalls,
        'replacements': replacements,
        'student_pcs': student_pcs,
        #'all_replacement': all_replacement
    }
    return render(request, 'GDR/my_replacements.html', context)


@login_required
def add_replacement(request):
    return render(request, 'GDR/add_replacement.html')


@login_required
def add_reinstall(request):
    return render(request, 'GDR/add_reinstall.html')


@login_required
def add_install(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = InstallForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('index')

        # if a GET (or any other method) we'll create a blank form
    else:
        form = InstallForm()
    return render(request, 'GDR/add_install.html', {'form': form})


@login_required
def add_student_pc(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = PcStudentsForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('index')

        # if a GET (or any other method) we'll create a blank form
    else:
        form = PcStudentsForm()
    return render(request, 'GDR/add_student_pc.html', {'form': form})
