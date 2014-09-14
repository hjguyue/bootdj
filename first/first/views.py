from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from django.shortcuts import render_to_response
import datetime

from books.models import Publisher

def hello(request):
    return HttpResponse("Hello world")

def display_meta(request):
    values = request.META.items()
    values.sort()
    html = []
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))
    # return HttpResponse(request.get_full_path() + "")

def showDB(request):
    objects = Publisher.objects.all()
    return render_to_response("current_datetime.html", locals())

def current_datetime(request):
    # now = datetime.datetime.now()
    # html = "<html><body>It is now %s.</body></html>" % now
    # return HttpResponse(html)
    
    # now = datetime.datetime.now()
    # t = get_template('current_datetime.html')
    # html = t.render(Context({'current_date': now}))
    # return HttpResponse(html)

    current_date = datetime.datetime.now()
    return render_to_response("current_datetime.html", locals())

# def search_form(request):
#     return render_to_response("search_form.html", locals())

def search(request):
    errors = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append('Enter a search term.')
        elif len(q) > 20:
            errors.append('Please enter at most 20 characters.')
        else:
            publishers = Publisher.objects.filter(name__icontains=q)
            return render_to_response("search_results.html", {'publishers':publishers, "q":q})
    return render_to_response('search_form.html', {'errors': errors})

