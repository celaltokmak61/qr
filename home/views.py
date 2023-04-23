from django.shortcuts import render
from .models import about , galeri_name, galeri, reference

# Create your views here.
def index(request):
    abouts = about.objects.first()
    galeri_names = galeri_name.objects.all()
    galeris = galeri.objects.filter(is_active=True)
    category= galeri.objects.get(is_active=True).category.all()
    references = reference.objects.all()

    return render(request, 'index.html', {'abouts': abouts, 'name': galeri_names, 'galeris': galeris, 'category': category, 'reference': references })

def services(request):
    return render(request, 'services.html')

def pricing(request):
    return render(request, 'pricing.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')