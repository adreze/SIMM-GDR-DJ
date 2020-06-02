from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from GDR.forms import PcStudentsForm, InstallForm, ReinstallForm, ReplacementForm
from GDR.models import Install, StudentPC, Replacement, Reinstall

#from .forms import UserForm


@login_required
def index(request):
    current_team_abv = check_team_abv(request)
    current_team = check_team(request)
    #Install.objects.filter(id=1).delete()
    #if the order_by doesn't work try -dateplanned
    installs = Install.objects.filter(byteam=current_team_abv).order_by('dateplanned')
    reinstalls = Reinstall.objects.filter(byteam=current_team_abv).order_by('dateplanned')
    replacements = Replacement.objects.filter(byteam=current_team_abv).order_by('dateplanned')
    student_pcs = StudentPC.objects.filter(byteam=current_team_abv).order_by('dateplanned')
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
    url = reverse('index')
    current_team_abv = check_team_abv(request)
    if request.method == 'POST':
        form = ReplacementForm(request.POST)
        if form.is_valid():
            p = form.save(commit=False)
            p.simmuser = request.user
            p.byteam = current_team_abv
            p.type = "Rep"
            p.save()
            return HttpResponseRedirect(url)
        # if a GET (or any other method) we'll create a blank form
    else:
        form = ReplacementForm()
    return render(request, 'GDR/add_replacement.html', {'form': form})


@login_required
def add_reinstall(request):
    url = reverse('index')
    current_team_abv = check_team_abv(request)
    if request.method == 'POST':
        form = ReinstallForm(request.POST)
        if form.is_valid():
            p = form.save(commit=False)
            p.simmuser = request.user
            p.byteam = current_team_abv
            p.type = "Reins"
            p.save()
            return HttpResponseRedirect(url)
        # if a GET (or any other method) we'll create a blank form
    else:
        form = ReinstallForm()
    return render(request, 'GDR/add_reinstall.html', {'form': form})


@login_required
def add_install(request):
    url = reverse('index')
    current_team_abv = check_team_abv(request)
    if request.method == 'POST':
        form = InstallForm(request.POST)
        if form.is_valid():
            p = form.save(commit=False)
            p.simmuser = request.user
            p.byteam = current_team_abv
            p.type = "Ins"
            p.save()
            return HttpResponseRedirect(url)
        # if a GET (or any other method) we'll create a blank form
    else:
        form = InstallForm()
    return render(request, 'GDR/add_install.html', {'form': form})


@login_required
def add_student_pc(request):
    url = reverse('index')
    current_team_abv = check_team_abv(request)
    if request.method == 'POST':
        form = PcStudentsForm(request.POST)
        if form.is_valid():
            p = form.save(commit=False)
            p.simmuser = request.user
            p.byteam = current_team_abv
            p.type = "Stud"
            p.save()
            return HttpResponseRedirect(url)
    else:
        form = PcStudentsForm()
    return render(request, 'GDR/add_student_pc.html', {'form': form})


def check_team(request):
    current_team = "Aucune"
    if request.user.groups.filter(name="SIMM-Centre").exists():
        current_team = "SIMM-Centre"
    if request.user.groups.filter(name="SIMM-Mercier").exists():
        current_team = "SIMM-Mercier"
    if request.user.groups.filter(name="SIMM-MO").exists():
        current_team = "SIMM-MO"
    return current_team


def check_team_abv(request):
    current_team_abv = "Aucune"
    if request.user.groups.filter(name="SIMM-Centre").exists():
        current_team_abv = "CE"
    if request.user.groups.filter(name="SIMM-Mercier").exists():
        current_team_abv = "ME"
    if request.user.groups.filter(name="SIMM-MO").exists():
        current_team_abv = "MO"
    return current_team_abv