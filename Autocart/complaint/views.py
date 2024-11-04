from django.shortcuts import render
from complaint.models import Complaint
import datetime

# Create your views here.
def add_complaint(request):
    uid=request.session["u_id"]
    if request.method == 'POST':
        obj = Complaint()
        obj.complaint = request.POST.get('complaint')
        obj.replay = 'pending'
        obj.customer_id = uid
        obj.date = datetime.date.today()
        obj.time = datetime.datetime.now()
        obj.save()
    return render(request, 'complaint/add_complaint.html')



def post_replay(request,idd):
    if request.method == 'POST':
        obj = Complaint.objects.get(complaint_id=idd)
        obj.replay =request.POST.get('postrply')
        obj.save()
        return view_complaint(request)

    return render(request, 'complaint/post_replay.html')



def view_complaint(request):
    obj = Complaint.objects.all()
    context = {
        'a': obj
    }
    return render(request, 'complaint/view_complaint.html', context)



def view_replay(request):
    uid=request.session["u_id"]
    obj = Complaint.objects.filter(customer_id=uid)
    context = {
        'ab': obj
    }
    return render(request, 'complaint/view_replay.html',context)

