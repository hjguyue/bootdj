from django.core.mail import send_mail
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect

# Create your views here.

def contact(request):
    # errors = []
    # if 'q' in request.GET:
    #     q = request.GET['q']
    #     if not q:
    #         errors.append('Enter a search term.')
    #     elif len(q) > 20:
    #         errors.append('Please enter at most 20 characters.')
    #     else:
    #         publishers = Publisher.objects.filter(name__icontains=q)
    #         return render_to_response("search_results.html", {'publishers':publishers, "q":q})
    errors = []
    if request.method == "POST":
        if not request.POST.get('subject', ''):
            errors.append('Enter a subject.') 
        if not request.POST.get('message', ''):
            errors.append('Enter a message.')
        if request.POST.get('email') and '@' not in request.POST['email']:
            errors.append('Enter a valid e-mail address.')
        if not errors:
            # send_mail(
            #     request.POST['subject'], 
            #     request.POST['message'], 
            #     request.POST.get('email', 'noreply@example.com'),
            #     ['siteowner@example.com'],
            #     )
            return HttpResponseRedirect('thanks/')
    return render_to_response('contact_form.html', {'errors': errors})

def thanks(request):
    return render_to_response('thanks.html')