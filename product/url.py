from django.conf.urls import url
from product import views

urlpatterns=[
    url('product/',views.product),
    url('view/',views.view_product),
    url('view_user/',views.view_product_user),
    url('add_to_cart/(?P<idd>\w+)',views.add_to_cart),
    url('cart_vw/',views.view_cart),
    url('remove/(?P<idd>\w+)',views.remove),
    url('rating/(?P<idd>\w+)',views.rating),
    url('view_rat/', views.view_rating)
    
    
]