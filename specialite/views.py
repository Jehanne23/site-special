from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def spe_maths(request):
    return render(request, 'spe_maths.html')

def spe_nsi(request):
    return render(request, 'spe_nsi.html')

def spe_pc(request):
    return render(request, 'spe_pc.html')
