from django.db import models

# Create your models here.

class About(models.Model):
    company = models.CharField(max_length=30)
    content = models.TextField()
    about_image = models.CharField(max_length=250)

    def __str__(self):
        return self.company

class GalleryType(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Gallery(models.Model):
    is_active = models.BooleanField(default=True)
    category = models.ManyToManyField(GalleryType)
    image = models.TextField(max_length=250)    
    image_name = models.CharField(max_length=30)

    def __str__(self):
        return self.image_name
    
class Reference(models.Model):
    name = models.CharField(max_length=30)
    image = models.TextField(max_length=250)

    def __str__(self):
        return self.name    
    
class Planing(models.Model):
    title = models.CharField(max_length=30)
    property1 = models.CharField(max_length=250)
    property2 = models.CharField(max_length=250)
    property3 = models.CharField(max_length=250)
    property4 = models.CharField(max_length=250)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    
class Services(models.Model):
    name = models.CharField(max_length=50, default="Services")
    title1 = models.CharField(max_length=50)
    content1 = models.TextField()
    title2 = models.CharField(max_length=50)
    content2 = models.TextField()
    title3 = models.CharField(max_length=50)
    content3 = models.TextField()

    def __str__(self):
        return self.name 
