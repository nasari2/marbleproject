from django.shortcuts import render

# Create your views here.
# rzp_test_Ey8ivDWGODPlAZ == api
# ttmCr5Cy7mQYI2Eck7W6UD3u == sec

from django.shortcuts import render
from order.models import Order
from payment.models import Payment
from django.conf import settings
import datetime
import razorpay

def payment_form(request,idd):
    uid=request.session["u_id"]
    razorpay_key = 'rzp_test_Ey8ivDWGODPlAZ'
    ob=Order.objects.get(o_id=idd)
    qty=int(ob.quantity)
    # amount=ob.p.p_name
    amount = (int(ob.p.p_price)*100)*qty
    context={
        'razorpay_key': razorpay_key,
        'amt':str(amount)
    }
    obj=Payment()
    obj.o_id=idd
    obj.u_id=uid
    obj.status='pending'
    obj.amount=amount
    obj.date_time=datetime.datetime.now()
    # obj.owner_id=ob.route.owner_id
    obj.save()
    request.session['payid']=str(obj.payment_id)
    return render(request, 'paymentrazor.html', context)

from django.http import JsonResponse
def update_payment(request):

    ob=Payment.objects.get(payment_id=request.session['payid'])
    ob.status='paid'
    ob.save()
    obj = Order.objects.get(o_id=ob.o_id)
    obj.status='paid'
    obj.save()
    msg = {

        'al': 'Payment completed Successfully',
    }
    return JsonResponse(msg)