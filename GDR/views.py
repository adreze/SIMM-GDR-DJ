from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import authenticate
from GDR.models import User
from django.views.generic import TemplateView
from .forms import UserForm

def index(request):
    return HttpResponse("Hello, world. You're at the GDR's index.")


def login(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request, 'registration/login.html', context)


# def login_in(request):
#     user = authenticate(username='john', password='secret')
#     if user is not None:
#     # A backend authenticated the credentials
#     else:


# No backend authenticated the credentials


def user_list(request):
    users = User.objects.all()
    context = {
        'users': users
    }
    return render(request, 'GDR/users_list.html', context)


class AboutView(TemplateView):
    template_name = "login.html"

# def index(request):
#     template = loader.get_template('GDR/index.html')
#     return HttpResponse(template.render(request))
