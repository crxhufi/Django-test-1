from django.shortcuts import render, redirect
from .models import QR
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Create your views here.

@login_required
def home(request):
    qrs = QR.objects.all()
    context = {
        "QR": qrs
    }

    return render(request, 'index.html', context=context)

def log_out(request):
    logout(request)
    return redirect('/')









