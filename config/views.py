from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse, HttpResponseRedirect  # Add this
# from django.http import request
from .forms import *  # Add this
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
            return HttpResponseRedirect('/signedup/')
    else:
        form = ContactForm()

    return render(request, 'pages/contact-us.html', {'form': form})


def org_contact(request):
    if request.method == 'POST':
        form = OrganizationForm(request.POST)
        if form.is_valid():
            # EMAIL CODE
            sender_name = form.cleaned_data['name']
            sender_email = form.cleaned_data['contact_email']
            org_name = form.cleaned_data['organization_name']
            posture_choices = form.cleaned_data['posture_and_ergonomics']
            stress = form.cleaned_data['stress_reduction']
            attention = form.cleaned_data['attention_and_focus']
            city = form.cleaned_data['city']

            message = "{0} from {6} has sent you a new message:\n\nMessage: {1}\n" \
                      "Posture choices: {2}\n" \
                      "Stress reduction choices: {3}\n" \
                      "Attention and focus choices: {4}\n" \
                      "City: {5}".format(sender_name, form.cleaned_data['message'],
                                         posture_choices, stress, attention, city, org_name)

            send_mail('New Enquiry from Organization', message, sender_email, ['austin.haw@gmail.com'])
            return HttpResponseRedirect('/signedup/')
    else:
        form = OrganizationForm()

    return render(request, 'pages/organization-form.html', {'form': form})


def prac_contact(request):
    if request.method == 'POST':
        form = PractitionerForm(request.POST)
        if form.is_valid():
            # EMAIL CODE
            sender_name = form.cleaned_data['name']
            sender_email = form.cleaned_data['email']
            # org_name = form.cleaned_data['organization_name']
            posture_choices = form.cleaned_data['posture_and_ergonomics']
            stress = form.cleaned_data['stress_reduction']
            attention = form.cleaned_data['attention_and_focus']
            city = form.cleaned_data['city']

            message = "{0} has sent you a new message:\n\nMessage: {1}\n" \
                      "Posture choices: {2}\n" \
                      "Stress reduction choices: {3}\n" \
                      "Attention and focus choices: {4}\n" \
                      "City: {5}".format(sender_name, form.cleaned_data['message'],
                                         posture_choices, stress, attention, city)

            send_mail('New Enquiry from Practitioner', message, sender_email, ['austin.haw@gmail.com'])
            return HttpResponseRedirect('/signedup/')
        # else:
        #     print("FORM NOT VALID")
    else:
        form = PractitionerForm()

    return render(request, 'pages/practitioner-form.html', {'form': form})
