from django.conf.urls import url
from order import views

urlpatterns=[
    url('order/(?P<idd>\w+)',views.order),
    url('view_order_details/',views.view_order_details),
    url('view_order_status/',views.view_order_status),
    url('view_delivery_status/', views.view_delivery_status),
    url('accept/(?P<idd>\w+)', views.accept),
    url('reject/(?P<idd>\w+)', views.reject),
    url('new/',views.newpage)

]