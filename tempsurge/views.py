from django.shortcuts import render, redirect


def home(request):
    return redirect('sign_in')


def home_old(request):
    return redirect('/pages/home/')