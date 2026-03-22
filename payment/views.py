from django.shortcuts import render
from payment.models import Payment
import datetime
# Create your views here.

def payment(request, idd):
    ss = request.session["u_id"]
    if request.method=="POST":
        obj=Payment()
        obj.amount=request.POST.get('amount')
        obj.u_id=ss
        obj.o_id=idd
        obj.date_time=datetime.datetime.today()
        obj.save()
    return render(request,'payment/payment.html')

def view_payment(request):
    obj=Payment.objects.all()
    context={
        'a':obj
    }
    return render(request,'payment/view_payment.html',context)