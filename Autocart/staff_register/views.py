from django.shortcuts import render
from staff_register.models import StaffRegister
from login.models import Login



# Create your views here.
def staff_register(request):
    if request.method == "POST":
        uname=request.POST.get('uname')
        if Login.objects.filter(username=uname).exists():
            message="Username already exist"
        else:
            ob = StaffRegister()
            ob.staff_name = request.POST.get('uname')
            ob.staff_address = request.POST.get('address')
            ob.staff_phonenumber = request.POST.get('sphnum')
            ob.staff_dateofbirth = request.POST.get('s_dob')
            ob.staff_gender = request.POST.get('gender')
            ob.staff_email = request.POST.get('smail')
            ob.user_name = request.POST.get('uname')
            ob.password = request.POST.get('pwd')
            ob.city = request.POST.get('scity')
            ob.save()

            obj=Login()
            obj.username=ob.user_name
            obj.password=ob.password
            obj.type='staff'
            obj.uid =ob.staff_id
            obj.save()

            message="successfully registered"
        context={
            'msg':message
        }
        return render(request,'staff_register/staff_register.html',context)
    return render(request, 'staff_register/staff_register.html')


def update_profile(request, idd):
    obj = StaffRegister.objects.get(staff_id=idd)
    context = {
        'a': obj
    }
    if request.method == "POST":
        ob = StaffRegister.objects.get(staff_id=idd)
        ob.staff_name = request.POST.get('sname')
        ob.staff_address = request.POST.get('address')
        ob.staff_phonenumber = request.POST.get('sphnum')
        ob.staff_dateofbirth = request.POST.get('s_dob')
        ob.staff_gender = request.POST.get('gender')
        ob.staff_email = request.POST.get('smail')
        ob.city = request.POST.get('scity')
        ob.save()
        return view_updatedprofile(request)


    return render(request, 'staff_register/update_profile.html', context)

def view_updatedprofile(request):
    obj = StaffRegister.objects.all()
    context = {
        'al' : obj
    }
    return render(request, 'staff_register/view_updateprofile.html',context)

def  delete(request, idd):
    ob = StaffRegister.objects.get(staff_id=idd)
    ob.delete()
    return view_updatedprofile(request)