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

    def test_delete(self):
        '''
        test object can be deleted  from database 
        '''
        self.category.save_category()
        self.category = Category.objects.get(id = 1)
        self.category.delete_category()
        self.assertTrue(len(Category.objects.all())== 0)




        