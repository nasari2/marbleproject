from django.http import HttpResponseRedirect
from django.shortcuts import render
from event.models import Event
import datetime
# Create your views here.

def event(request, idd):
    ss = request.session["event_id"]
    if request.method=="POST":
        obj=event()
        obj.event_type = request.POST.get('type')
        obj.name = request.POST.get('price')
        # obj.quantity=request.POST.get('qnty')
        # obj.date_time=datetime.datetime.today()
        obj.status="pending"
        obj.save()
        return HttpResponseRedirect('/paymentrazor/payment-form/'+str(obj.event_id))
    return render(request,'event/event.html')

# def view_order_details(request):
#     obj=event.objects.all()
#     context={
#         'a':obj
#     }
#     return render(request,'event/view_event_details.html',context)

# Create your views here.
