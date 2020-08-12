from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from GDR.forms import PcStudentsForm, InstallForm, ReinstallForm, ReplacementForm
from GDR.models import Install, StudentPC, Replacement, Reinstall


filter_on = False

@login_required
def index(request):
    typeselected = False
    if request.method == 'GET':
        typeselected = request.GET.get('type')
    current_team_abv = check_team_abv(request)
    current_team = check_team(request)

    if typeselected == "Ins":
        installs = Install.objects.filter(byteam=current_team_abv).order_by('dateplanned')
        context = {
            'installs': installs,
            'current_team': current_team
        }
    elif typeselected == "Reins":
        reinstalls = Reinstall.objects.filter(byteam=current_team_abv).order_by('dateplanned')
        context = {
            'reinstalls': reinstalls,
            'current_team': current_team
        }
    elif typeselected == "Rep":
        replacements = Replacement.objects.filter(byteam=current_team_abv).order_by('dateplanned')
        context = {
            'replacements': replacements,
            'current_team': current_team
        }
    elif typeselected == "Stud":
        student_pcs = StudentPC.objects.filter(byteam=current_team_abv).order_by('dateplanned')
        context = {
            'student_pcs': student_pcs,
            'current_team': current_team
        }
    else:
        installs = Install.objects.filter(byteam=current_team_abv).order_by('dateplanned')
        reinstalls = Reinstall.objects.filter(byteam=current_team_abv).order_by('dateplanned')
        replacements = Replacement.objects.filter(byteam=current_team_abv).order_by('dateplanned')
        student_pcs = StudentPC.objects.filter(byteam=current_team_abv).order_by('dateplanned')
        context = {
            'installs': installs,
            'reinstalls': reinstalls,
            'replacements': replacements,
            'student_pcs': student_pcs,
            'current_team': current_team
    }
    return render(request, 'GDR/index.html', context)


@login_required
def my_replacements(request):
    typeselected = False
    if request.method == 'GET':
        typeselected = request.GET.get('type')
    current_team_abv = check_team_abv(request)
    current_team = check_team(request)

    if typeselected == "Ins":
        installs = Install.objects.filter(simmuser=request.user).order_by('dateplanned')
        context = {
            'installs': installs,
        }
    elif typeselected == "Reins":
        reinstalls = Reinstall.objects.filter(simmuser=request.user).order_by('dateplanned')
        context = {
            'reinstalls': reinstalls,
        }
    elif typeselected == "Rep":
        replacements = Replacement.objects.filter(simmuser=request.user).order_by('dateplanned')
        context = {
            'replacements': replacements,
        }
    elif typeselected == "Stud":
        student_pcs = StudentPC.objects.filter(simmuser=request.user).order_by('dateplanned')
        context = {
            'student_pcs': student_pcs,
        }
    else:
        installs = Install.objects.filter(simmuser=request.user).order_by('dateplanned')
        reinstalls = Reinstall.objects.filter(simmuser=request.user).order_by('dateplanned')
        replacements = Replacement.objects.filter(simmuser=request.user).order_by('dateplanned')
        student_pcs = StudentPC.objects.filter(simmuser=request.user).order_by('dateplanned')
        context = {
            'installs': installs,
            'reinstalls': reinstalls,
            'replacements': replacements,
            'student_pcs': student_pcs,
        }
    return render(request, 'GDR/my_replacements.html', context)


@login_required
def add_replacement(request):
    url = reverse('my_replacements')
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
    else:
        form = ReplacementForm()
    return render(request, 'GDR/add_replacement.html', {'form': form})


@login_required
def add_reinstall(request):
    url = reverse('my_replacements')
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
    else:
        form = ReinstallForm()
    return render(request, 'GDR/add_reinstall.html', {'form': form})


@login_required
def add_install(request):
    url = reverse('my_replacements')
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
    else:
        form = InstallForm()
    return render(request, 'GDR/add_install.html', {'form': form})


@login_required
def add_student_pc(request):
    url = reverse('my_replacements')
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


@login_required
def edit(request, type_p, id_p):
    url = reverse('my_replacements')
    form_selected = "Aucun"
    db_selected = "Aucun"
    template_selected = 'GDR/index.html'

    if type_p == "Ins":
        form_selected = InstallForm
        db_selected = Install
        template_selected = 'GDR/edit_install.html'
    if type_p == "Reins":
        form_selected = ReinstallForm
        db_selected = Reinstall
        template_selected = 'GDR/edit_reinstall.html'
    if type_p == "Rep":
        form_selected = ReplacementForm
        db_selected = Replacement
        template_selected = 'GDR/edit_replacement.html'
    if type_p == "Stud":
        form_selected = PcStudentsForm
        db_selected = StudentPC
        template_selected = 'GDR/edit_student_pc.html'
    instance = db_selected.objects.get(id=id_p)

    if request.method == "POST":
        form = form_selected(request.POST, instance=instance)
        form.save()
        return HttpResponseRedirect(url)
    else:
        form = form_selected(instance=instance)
    return render(request, template_selected, {'form': form})


@login_required
def delete(request, type_p, id_p):
    url = reverse('my_replacements')
    if type_p == "Ins":
        db_selected = Install
    elif type_p == "Reins":
        db_selected = Reinstall
    elif type_p == "Rep":
        db_selected = Replacement
    elif type_p == "Stud":
        db_selected = StudentPC
    else:
        db_selected = "Aucun"
    db_selected.objects.filter(id=id_p).delete()
    return HttpResponseRedirect(url)


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


def filter(request):
    typeselected = request.GET.get('type')
    if typeselected == "Ins":
        db_selected = Install
    elif typeselected == "Reins":
        db_selected = Reinstall
    elif typeselected == "Rep":
        db_selected = Replacement
    elif typeselected == "Stud":
        db_selected = StudentPC
    return typeselected.objects.all()
