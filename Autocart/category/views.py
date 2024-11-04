from django.shortcuts import render
from category.models import Category

# Create your views here

def category(request):
    if request.method == 'POST':
        obj = Category()
        obj.category = request.POST.get('addcat')
        obj.save()
    return render(request, 'category/add_category.html')