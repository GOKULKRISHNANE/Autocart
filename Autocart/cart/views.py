from django.shortcuts import render, redirect
from cart.models import Cart
import datetime
# Create your views here.
# def cart(request):
#     if request.method == 'POST':
#         obj = Cart()
#         obj.product_id = 1
#         obj.date = datetime.datetime.today()
#         obj.time = datetime.datetime.now()
#         obj.quantity = request.POST.get('qnty')
#         obj.save()
#     return render(request, 'cart/add_to_cart.html')

def viewcart(request):
    obj = Cart.objects.all()
    context = {
        'ac':obj
    }
    return render(request, 'cart/view_cart.html', context)

def checkout_view(request):
    if request.method == 'POST':
        # Delete all items in the cart (assuming 'CartItem' model)
        Cart.objects.all().delete()
        # Redirect to a success page or any other appropriate action
        return render(request,'cart/view_cart.html')
    # Handle GET request if needed
    return render(request,'cart/view_cart.html')