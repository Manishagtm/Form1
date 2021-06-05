from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import LoginForm, SignForm


# Create your views here.
# def form(request):
# return render(request, 'form.html')


#


def two(request):
    return render(request, 'two.html')


def form(response):
    if response.method == "POST":

        form1 = LoginForm(response.POST)
        if form1.is_valid():
            form1.save()

        return redirect('')
    else:
        form1 = LoginForm()

    return render(response, 'form.html', {'form1': form1})


def sign(response):
    if response.method == "POST":

        form2 = SignForm(response.POST)
        if form2.is_valid():
            form2.save()

        return redirect('')
    else:
        form2 = SignForm()

    return render(response, 'sign.html', {'form2': form2})

