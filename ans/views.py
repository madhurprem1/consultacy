from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Contact
from .forms import ContactFrom
from django.contrib import messages
# from django.urls import reverse_lazy
# Create your views here.


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def career(request):
    return render(request, 'career.html')


def staffing(request):
    return render(request, 'staffing.html')


def productdevelopment(request):
    return render(request, 'productdevelopment.html')


def projectmanagement(request):
    return render(request, 'projectmanagement.html')


def itconsulting(request):
    return render(request, 'itconsulting.html')


def contact(request):
    print(request.method)
    if request.method == 'GET':
        form = ContactFrom()
    else:
        form = ContactFrom(request.POST)
        print(5555555555555)
        print(form)
        if form.is_valid():
            print(22222)
            name = form.cleaned_data['name']
            from_email = form.cleaned_data['from_email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            # success_url = reverse_lazy("thanks")
            try:
                send_mail(subject, message, from_email, ['madhurprem1@gmail.com'])
                print(33333333333)
            except BadHeaderError:
                return HttpResponse('Invalid header found !')
            m = Contact(name=name, from_email=from_email, subject=subject, message=message)
            m.save()
            print(111111111)
            messages.success(request, 'Your form was saved successfully!', extra_tags='alert')
            # messages.add_message(request, message.SUCCESS, 'Your form was saved successfully')
            # print(message)
            return redirect('contact')
    return render(request, 'contact.html', {'form': form})


def successView(request):

    return HttpResponse('Success! Thank you for your message.')
    # return render(request, 'contact.html')




