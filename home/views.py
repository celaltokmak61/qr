from django.shortcuts import render
from .models import About , GalleryType, Gallery, Reference

# Create your views here.
def index(request):
    abouts = About.objects.first()
    galeri_names = GalleryType.objects.all()
    galeris = Gallery.objects.filter(is_active=True)
    category= Gallery.objects.get(is_active=True).category.all()
    references = Reference.objects.all()

    return render(request, 'index.html', {'abouts': abouts, 'name': galeri_names, 'galeris': galeris, 'category': category, 'reference': references })

def services(request):
    return render(request, 'services.html')

def pricing(request):
    return render(request, 'pricing.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')