from django.shortcuts import render
from bill.models import Bill

# Create your views here.

def view_bill_admin(request):
    obj = Bill.objects.all()
    context = {
        'a':obj
    }
    return render(request, 'bill/bill_admin.html',context)


def view_bill_staff(request):
    obj = Bill.objects.all()
    context = {
        'a':obj
    }
    return render(request, 'bill/bill_staff.html',context)

def view_bill_customer(request):
    obj = Bill.objects.all()
    context = {
        'a':obj
    }
    return render(request, 'bill/bill_user.html',context)