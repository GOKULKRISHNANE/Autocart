from django.shortcuts import render
from customer.models import  Customer
from login.models import Login

# Create your views here.
def customer(request):
    if request.method == 'POST':
        uname=request.POST.get('usrname')
        if Login.objects.filter(username=uname).exists():
            message="Username already exist"
        else:
            obj = Customer()
            obj.customer_username = request.POST.get('usrname')
            obj.customer_password = request.POST.get('pwd')
            obj.customer_name = request.POST.get('uname')
            obj.customer_dateofbirth = request.POST.get('u_dob')
            obj.customer_address = request.POST.get('address')
            obj.customer_city = request.POST.get('ucity')
            obj.customer_gender = request.POST.get('gender')
            obj.field_customer_phonenumber = request.POST.get('uphnum')
            obj.save()

            ob=Login()
            ob.username=obj.customer_username
            ob.password=obj.customer_password
            ob.type='customer'
            ob.uid=obj.customer_id
            ob.save()

            message="Successfully registered"
        context={
            'msg':message
        }
        return render(request, 'customer/customer_register.html',context)

    return render(request, 'customer/customer_register.html')