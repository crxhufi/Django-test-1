from django.shortcuts import render, redirect
from urllib.parse import unquote
from .models import QR
from django.contrib.auth import authenticate, login

# Create your views here.

def home(request):
    qrs = QR.objects.all()
    context = {
        "QR": qrs
    }

    return render(request, 'index.html', context=context)









