from django.contrib import admin
from .models import About, GalleryType, Gallery, Reference, Planing, Services

# Register your models here.

admin.site.register(About)
admin.site.register(GalleryType)
admin.site.register(Gallery)
admin.site.register(Reference)
admin.site.register(Planing)
admin.site.register(Services)