from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def services(request):
    return render(request, 'services.html')

def pricing(request):
    return render(request, 'pricing.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')