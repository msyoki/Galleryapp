from django.shortcuts import render
from .models import Image

# Create your views here.

def galla(request):
    images = Image.get_all_images()
    test='Gallery'
    return render(request, 'index.html',{'images': images,'test': test})
