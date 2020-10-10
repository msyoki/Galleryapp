from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Location(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Image(models.Model):
    images = models.ImageField(upload_to = 'photos/',null =True)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    category= models.ForeignKey('Category',on_delete = models.CASCADE, null='True', blank=True)
    location= models.ForeignKey('Location',on_delete = models.CASCADE, null='True', blank=True)

    def __str__(self):
        return self.name