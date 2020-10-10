from django.shortcuts import render
from .models import Image,Category

# Create your views here.

def galla(request):
    images = Image.get_all_images()
    test='Gallery'
    return render(request, 'index.html',{'images': images,'test': test})

def search_category(request):
    if 'category' in request.GET and request.GET["category"]:
        search_term = request.GET.get("category")
        searched_images = Image.search_by_category(search_term)
        message = f"{search_term}"
        
        return render(request,'category.html',{"message":message, "images":searched_images, "category":search_term})
    
    else:
        message = "Please search category"
        
        return render(request, 'category.html', {"message":message})