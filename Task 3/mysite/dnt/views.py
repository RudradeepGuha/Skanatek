from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def index(request):
    template = loader.get_template('dnt/index.html')
    context = {'time': '10:10',}
    return HttpResponse(template.render(context, request))
