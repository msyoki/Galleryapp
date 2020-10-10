from django.shortcuts import render
from .models import Image

# Create your views here.

def galla(request):
    all_photos = Image.all_photos()
    print(all_photos)
    return render(request, 'index.html',{"all_photos":all_photos})