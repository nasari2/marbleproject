from django.conf.urls import url
from payment import views

urlpatterns=[
    url('payment/(?P<idd>\w+)',views.payment),
    url('view/',views.view_payment)
    
    
]