from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# def index(request):
#     return HttpResponse("Hello, world. You're at the GDR's index.")


def index(request):
    template = loader.get_template('GDR/index.html')
    return HttpResponse(template.render(request))
