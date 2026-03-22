from django.conf.urls import url
from temp import views

urlpatterns = [
    url('home/', views.home),
    url('admin/', views.admin),
    url('delivery_boy/', views.delivery_boy),
    url('user/', views.user),
    url('ooo/',views.oooooo),
    url('pppp/',views.ppppp),
    url('update/(?P<idd>\w+)',views.update_product),
    url('rat/', views.view_rating)
]