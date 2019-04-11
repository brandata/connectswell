from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse  # Add this
from django.http import request
from .forms import ContactForm  # Add this
from django.core.mail import send_mail


def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # EMAIL CODE
            sender_name = form.cleaned_data['name']
            sender_email = form.cleaned_data['email']

            message = "{0} has sent you a new message:\n\n{1}".format(sender_name, form.cleaned_data['message'])
            send_mail('New Enquiry', message, sender_email, ['brandon.haw@gmail.com'])
            return HttpResponse('Thanks for contacting us!')
    else:
        form = ContactForm()

    return render(request, 'pages/contact-us.html', {'form': form})
