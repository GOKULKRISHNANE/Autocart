from django.shortcuts import render
from login.models import Login
from django.http import HttpResponseRedirect


# Create your views here.
def login(request):
    if request.method == "POST":
        uname = request.POST.get("uname")
        passw = request.POST.get("pwd")
        obj = Login.objects.filter(username=uname,password=passw)
        tp = ""
        for ob in obj:
            tp = ob.type
            uid = ob.uid
            if tp=="admin":
                request.session["u_id"] = uid
                return HttpResponseRedirect('/temp/admin/')
            elif tp == "customer":
                request.session["u_id"] = uid
                return HttpResponseRedirect('/temp/customer/')
            elif tp == "staff":
                request.session["u_id"] = uid
                return HttpResponseRedirect('/temp/staff/')
        else:
            objlist = "username or password incorrect........please try again.......!"
            context = {
                'msg': objlist
            }
            return render(request,'login/login.html', context)
    return render(request, 'login/login.html')