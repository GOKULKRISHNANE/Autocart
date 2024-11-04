from django.shortcuts import render
from payment.models import Payment
# Create your views here.
def add_payment(request):
    uid=request.session["u_id"]
    if request.method == "POST":
        ob=Payment()
        ob.customer_id = uid
        ob.bill_id = 1
        ob.amount = request.POST.get('amount')
        ob.type = request.POST.get('payment_type')
        ob.cart_number = request.POST.get('card_number')
        ob.cvv = request.POST.get('cvv')
        ob.status = 'paid'
        ob.save()
    return render(request, 'payment/payment.html')

def view_payment(request):
    obj = Payment.objects.all()
    context = {
        'ah' : obj
    }
    return render(request, 'payment/view_payment.html',context)