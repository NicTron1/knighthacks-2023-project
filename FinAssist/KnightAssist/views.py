from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def KnightAssist(request):
    template = loader.get_template('mainPage.html')
    return HttpResponse(template.render())