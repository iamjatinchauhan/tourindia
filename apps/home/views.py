from django.http import HttpResponse
from django.template import loader

# Create your views here.

def index(request):

    context = {'segment': 'index'}

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))
