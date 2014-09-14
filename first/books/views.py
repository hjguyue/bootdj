from django.shortcuts import render
from django.shortcuts import render_to_response
from books.models import Publisher

# Create your views here.

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
