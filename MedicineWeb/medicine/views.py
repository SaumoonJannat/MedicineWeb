from urllib import request
from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.views import View
from . models import Product,Customer,Cart
from django.db. models  import Count
from. forms import CustomerRegistrationForm,CustomerProfileForm
from django.contrib import messages
from django.db.models import Q


def home(request):
    return render(request,"app/home.html")

def about(request):
    return render(request,"app/about.html")

def contact(request):
    return render(request,"app/contact.html")

