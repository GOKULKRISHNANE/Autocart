from django.shortcuts import render

# Create your views here.
def admin(request):

    return render(request, 'temp/admin.html')

def customer(request):

    return render(request, 'temp/customer.html')


def home(request):
    return render(request, 'temp/home.html')


def staff(request):
    return render(request, 'temp/staff.html')