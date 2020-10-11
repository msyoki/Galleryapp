from django.test import TestCase
from .models import Category,Location,Image

# Create your tests here.
class CategoryTest(TestCase):
    '''
    Category class test
    '''
    def setUp(self):
        '''
        runs before each test
        ''' 
        self.category = Category(id = 1 ,name = "Cat")

    def test_instance(self):
        '''
        check object instance of category class
        '''
        self.assertTrue(isinstance(self.category,Category))

    def test_save(self):
        '''
        test if object is saved in database
        '''
        self.category.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) > 0)

    def test_update(self):
        '''
        test if object can be updated
        '''
        self.category.save_category()
        self.category = Category.objects.filter(name ='Cat').update(name='Cat1')
        self.updated_category = Category.objects.get(name='Cat1')
        self.assertEqual(self.updated_category.name,'Cat1')

    def test_delete(self):
        '''
        test object can be deleted  from db
        '''
        self.category.save_category()
        self.category = Category.objects.get(id = 1)
        self.category.delete_category()
        self.assertTrue(len(Category.objects.all())== 0)

class LocationTest(TestCase):
    '''
    location class test
    '''
    def setUp(self):
        '''
        runs before each test
        ''' 
        self.location = Location(id = 1 ,name = "Dubai")

    def test_instance(self):
        '''
        check object instance of location class
        '''
        self.assertTrue(isinstance(self.location,Location))

    def test_save(self):
        '''
        test if object is saved in  db
        '''
        self.location.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)

    def test_update(self):
        '''
        test if object can be updated
        '''
        self.location.save_location()
        self.location = Location.objects.filter(name ='Dubai').update(name='Italy')
        self.updated_location = Location.objects.get(name='Italy')
        self.assertEqual(self.updated_location.name,'Italy')

    def test_delete(self):
        '''
        test object can be deleted  from db 
        '''
        self.location.save_location()
        self.location = Location.objects.get(id = 1)
        self.location.delete_location()
        self.assertTrue(len(Location.objects.all())== 0)


class ImageTest(TestCase):
    '''
    Image class test
    '''
    def setUp(self):
        '''
        runs before the test
        ''' 
        self.category= Category(name='food')
        self.category.save_category()
        self.location= Location(name='China')
        self.location.save_location()

        self.image =Image(id=1,img= 'photos/a.jpeg',
        name = 'imagetest',
        description = 'test',
        category=self.category,
        location=self.location)


    def test_instance(self):
        '''
        check object instance of Image class
        '''
        self.assertTrue(isinstance(self.image,Image))

    def test_save(self):
        '''
        test if object can be saved in the db
        '''
        self.image.save_image()
        self.images=Image.objects.all()
        self.assertTrue(len(self.images) >0)


    def test_update(self):
       '''
       test if object can be updated from db
       '''
       self.image.save_image()
       self.image=Image.objects.filter(id=1).update(img='photos/b.jpeg') 
       self.updated_image=Image.objects.get(id=1)
       self.assertTrue(self.updated_image.img,'photos/b.jpeg')

    def test_delete(self):
        '''
        test if object can be deleted from db
        '''
        self.image.save_image()
        self.searched_image = Image.objects.get(id=1)
        self.searched_image.delete_image()
        self.assertTrue(len(Image.objects.all()) == 0)

    def test_search_by_category(self):
        '''
        test image filter by category
        '''
        self.image.save_image()
        self.category= Category(name='food')
        self.category.save_category()
        self.searched_images=Image.search_by_category('food')
        self.assertTrue(len(self.searched_images) > 0)
