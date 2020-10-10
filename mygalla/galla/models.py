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
    img = models.ImageField(upload_to = 'photos/',null =True)
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=400)
    category= models.ForeignKey('Category',on_delete = models.CASCADE, null='True', blank=True)
    location= models.ForeignKey('Location',on_delete = models.CASCADE, null='True', blank=True)

    
    @classmethod
    def get_all_images(cls):
        '''
          Method to return all the images.
        '''
        images = cls.objects.all()
        return images

    @classmethod
    def search_by_category(cls,search_term):
        '''
          Method to search for images based on their category.
        '''
        images = cls.objects.filter(category__name__icontains = search_term)
        
        return images

    
    def __str__(self):
        return self.name