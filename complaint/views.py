from django.shortcuts import render
from complaint.models import Complaint
import datetime
from order.models import Order

# Create your views here.

def complaint(request):
    obb = Order.objects.all()
    context = {
        'o': obb,
    }
    ss = request.session["u_id"]
    if request.method=="POST":
        obj=Complaint()
        obj.complaint=request.POST.get('cmpt')
        obj.date_time=datetime.datetime.today()
        obj.u_id=ss
        obj.o_id=1
        obj.reply='pending'
        obj.save()
    return render(request,'complaint/complaint.html',context)

def replypost(request,idd):
    if request.method=="POST":
        obj=Complaint.objects.get(c_id=idd)
        obj.reply=request.POST.get('reply')
        obj.save()
        return view_complaint(request)
    return render(request,'complaint/replypost.html')

def view_complaint(request):
    obj=Complaint.objects.all()
    context={
        'b':obj
    }

    return render(request,'complaint/view_complaint.html',context)

def view_reply(request):
    ss = request.session["u_id"]
    obj=Complaint.objects.filter(u_id=ss)
    contxt={
        'c':obj
    }
    return render(request,'complaint/view_reply.html',contxt)
    

