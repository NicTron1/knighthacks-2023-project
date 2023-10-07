#THIS IS THE FINASSIST VIEWS! NOT KNIGHTHACKS PROJECT VIEWS

from django.http import HttpResponse
from django.template import loader

def FinAssist(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())