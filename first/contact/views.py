from django.core.mail import send_mail
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect

from forms import ContactForm

# Create your views here.

def contact(request):
    # errors = []
    # subject = ''
    # message = ''
    # email = ''

    # if request.method == "POST":
    #     subject = request.POST.get('subject', '')
    #     if not subject:
    #         errors.append('Enter a subject.') 

    #     message = request.POST.get('message', '')
    #     if not message:
    #         errors.append('Enter a message.')

    #     email = request.POST.get('email','')
    #     if email and '@' not in request.POST['email']:
    #         errors.append('Enter a valid e-mail address.')
        
    #     if not errors:
    #         # send_mail(
    #         #     request.POST['subject'], 
    #         #     request.POST['message'], 
    #         #     request.POST.get('email', 'noreply@example.com'),
    #         #     ['siteowner@example.com'],
    #         #     )
    #         return HttpResponseRedirect('thanks/')
    # return render_to_response('contact_form.html', {'errors': errors, 'subject': subject, 'message':message, 'email':email})

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # cd = form.cleaned_data
            # send_mail(cd['subject'], ['message'], cd.get('email', 'hjguyue@sina.com'), ['hjguyue@gmail.com'],)
            return HttpResponseRedirect('thanks/')
    else:
        form = ContactForm(initial={'subject': 'I love your site!'})
    return render_to_response('contact_form.html', {'form':form})

def thanks(request):
    return render_to_response('thanks.html')