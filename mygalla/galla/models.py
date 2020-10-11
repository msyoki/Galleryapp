from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=40)

    def save_category(self):
        '''
        method to save category in db
        '''
        self.save()

    def update_category(self, test):
        '''
        method to update category in db
        '''
        self.update(name =test)


    def delete_category(self):
        ''''
        method to delete category in db
        '''
        self.delete()


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

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod
    def get_all_images(cls):
        '''
          Method to return all the images from db
        '''
        images = cls.objects.all()
        return images

    @classmethod
    def search_by_category(cls,search_term):
        '''
          Method to search for images based on their category from db
        '''
        images = cls.objects.filter(category__name__icontains = search_term)
        
        return images

    
    def __str__(self):
        return self.name