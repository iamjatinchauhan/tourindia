from django.http import HttpResponse
from django.template import loader
from django import template
# Create your views here.

def index(request):

    context = {'segment': 'index'}

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))


def pages(request):
    context = {'stage': 1}
    # All resource paths end in .html
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]  # picks the url of the template to be loaded

        context['segment'] = load_template
        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    # ##################// The above is the code that loads any template to the front end //############################
    # ##################################################################################################################

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))