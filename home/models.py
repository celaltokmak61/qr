from django.db import models

# Create your models here.

class about(models.Model):
    company = models.CharField(max_length=30)
    content = models.TextField()
    about_image = models.CharField(max_length=250)

    def __str__(self):
        return self.company

class galeri_name(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class galeri(models.Model):
    is_active = models.BooleanField(default=True)
    category = models.ManyToManyField("galeri_name")
    image = models.TextField(max_length=250)    
    imagename = models.CharField(max_length=30)

    def __str__(self):
        return self.imagename
    
class reference(models.Model):
    name = models.CharField(max_length=30)
    image = models.TextField(max_length=250)

    def __str__(self):
        return self.name    