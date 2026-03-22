from django.conf.urls import url
from event import views

urlpatterns = [
    url('event/', views.event),
    ]
    # url('view/', views.),
    # url('view_user/', views.view_product_user),

