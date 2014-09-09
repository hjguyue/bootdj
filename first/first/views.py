from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from django.shortcuts import render_to_response
import datetime


def hello(request):
    return HttpResponse("Hello world")

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