from django.shortcuts import render
from feedback.models import Feedback
import datetime
# Create your views here.
def add_feedback(request):
    uid=request.session["u_id"]
    if request.method == 'POST':
        obj = Feedback()
        obj.feedback = request.POST.get('feedback')
        obj.customer_id = uid
        obj.date = datetime.datetime.today()
        obj.time = datetime.datetime.now()
        obj.save()

    return render(request, 'feedback/add_feedback.html')


def view_feedback_staff(request):
    obj = Feedback.objects.all()
    context = {
        'ac': obj
    }
    return render(request, 'feedback/view_feedback(staff).html',context)


def view_feedback_admin(request):
    obj = Feedback.objects.all()
    context = {
        'ac': obj
    }

    return render(request, 'feedback/view_feedback.html',context)