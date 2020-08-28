from django.shortcuts import render
from .models import NewsletterUser
from .forms import NewletterUserSignUpForm
# Create your views here.


def newsletter_signup(request):
    form = NewletterUserSignUpForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        if NewsletterUser.objects.filter(email=instance.email).exsists():
            print("Sorry this email is already exsists !!")
        else:
            instance.save()
        context = {
            'form': form,
        }
        temlate = "signup.html"
        return render(request, temlate, context)


def newslwtter_unsuscribe(request):
    form = NewletterUserSignUpForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        if NewsletterUser.objects.filter(email=instance.email).exsists():
            NewsletterUser.objects.filter(email=instance.email).delete()
        else:
            print('sorry we did not found your email address !')
        context = {
            'form': form,
        }
        temlate = "unsuscribe.html"
        return render(request, temlate, context)