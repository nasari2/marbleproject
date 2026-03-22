from django.shortcuts import render
from user.models import User
from login.models import Login
from django.core.files.storage import FileSystemStorage
# Create your views here.

def user(request):
    if request.method=="POST":
        obj=User()
        obj.username=request.POST.get('uname')
        obj.u_place=request.POST.get('place')
        obj.u_district=request.POST.get('dis')
        obj.u_post=request.POST.get('post')
        obj.u_phone=request.POST.get('phone')
        obj.u_email=request.POST.get('email')
        # obj.u_proof=request.POST.get('proof')
        # myfile=request.FILES['proof']
        # fs=FileSystemStorage()
        # filename=fs.save(myfile.name,myfile)
        # obj.u_proof=myfile.name
        obj.password=request.POST.get('pas')
        obj.save()

        ob = Login()
        ob.username = obj.username
        ob.password = obj.password
        ob.u_id = obj.u_id
        ob.type = 'user'
        ob.save()
    return render(request,'user/user.html')

def view_user(request):
    obj=User.objects.all()
    context={
        'a':obj
    }
    return render(request,'user/view_user.html',context)