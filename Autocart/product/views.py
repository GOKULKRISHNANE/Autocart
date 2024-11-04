from django.shortcuts import render
from product.models import Product
from category.models import Category
from django.core.files.storage import FileSystemStorage

# Create your views here.
def add_product(request):
    obj=Category.objects.all()
    context={
        'x':obj
    }
    if request.method == "POST":
        ob = Product()
        ob.category_id = request.POST.get('ctg')
        ob.product_name = request.POST.get('p_name')
        myfile=request.FILES['filename']
        fs=FileSystemStorage()
        file_name=fs.save(myfile.name,myfile)
        ob.product_photo = myfile.name
        ob.product_price = request.POST.get('p_price')
        ob.product_quantity = request.POST.get('p_quant')
        ob.manufacturer_date = request.POST.get('p_mfd')
        ob.product_experity = request.POST.get('p_exp')
        ob.additional_description = request.POST.get('additional description')
        ob.save()

    return render(request, 'products/add_product.html',context)


def view_product_customer(request) :
    obj = Product.objects.all()
    context = {
        'af':obj
    }
    return render(request, 'products/view_product(cust).html',context)


def view_product(request) :
    obj = Product.objects.all()
    context = {
        'af' :obj
    }
    return render(request, 'products/view_product.html',context)


def view_product_admin(request) :
    obj = Product.objects.all()
    context = {
        'af':obj
    }
    return render(request, 'products/view_product(adm).html',context)
