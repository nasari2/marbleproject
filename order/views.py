from django.http import HttpResponseRedirect
from django.shortcuts import render
from order.models import Order
import datetime
# Create your views here.

def order(request, idd):
    ss = request.session["u_id"]
    if request.method=="POST":
        obj=Order()
        obj.quantity=request.POST.get('qnty')
        obj.u_id=ss
        obj.p_id=idd
        obj.date_time=datetime.datetime.today()
        obj.status="pending"
        obj.save()
        return HttpResponseRedirect('/paymentrazor/payment-form/'+str(obj.o_id))
    return render(request,'order/order.html')

def view_order_details(request):
    obj=Order.objects.all()
    context={
        'a':obj
    }
    return render(request,'order/view_order_details.html',context)

def view_order_status(request):
    ss = request.session["u_id"]
    obj=Order.objects.filter(u_id=ss)
    context={
        'a':obj
    }
    return render(request,'order/view_order_status.html',context)

def view_delivery_status(request):
    obj=Order.objects.all()
    context={
        'a':obj
    }
    return render(request,'order/view_delivery_status.html', context)

def newpage(request):
    obj=Order.objects.filter(status='accepted')
    context={
        'x':obj
    }
    return render(request,'order/new.html', context)

def accept(request,idd):
    obj = Order.objects.get(o_id=idd)
    obj.status = 'accepted'
    obj.save()
    return view_order_details(request)


def reject(request,idd):
    obj = Order.objects.get(o_id=idd)
    obj.status = 'rejected'
    obj.save()
    return view_order_details(request)









