from django.conf.urls import url
from complaint import views

urlpatterns=[
    url('complaint/',views.complaint),
    url('replypost/(?P<idd>\w+)',views.replypost),
    url('view/',views.view_complaint),
    url('view_reply/',views.view_reply)
    
    
    
    
    
]