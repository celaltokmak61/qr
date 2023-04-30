from django.shortcuts import render
from .models import About , GalleryType, Gallery, Reference, Planing, Services

# Create your views here.
def index(request):
    abouts = About.objects.first()
    galeri_names = GalleryType.objects.all()
    galeris = Gallery.objects.filter(is_active=True)
    category= Gallery.objects.filter(is_active=True)
    references = Reference.objects.all()

    return render(request, 'index.html', {'abouts': abouts, 'name': galeri_names, 'galeris': galeris, 'category': category, 'reference': references })

def services(request):
    service = Services.objects.first()

    return render(request, 'services.html', {'service': service})

def pricing(request):
    plans = Planing.objects.filter(is_active=True)

    return render(request, 'pricing.html', {'plans': plans})

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')