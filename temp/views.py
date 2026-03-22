from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from product.models import Product
from product.models import Rating
# Create your views here.

def home(request):
    return render(request,'temp/homenew.html')

def admin(request):
    return render(request,'temp/adminnew.html')

def delivery_boy(request):
    return render(request,'temp/deliverynew.html')

def user(request):
    return render(request,'temp/usernew.html')

def oooooo(request):
    obj=Product.objects.all()
    context={
        'j':obj
    }
    return render(request,'temp/usernew.html',context)


def ppppp(request):
    obj=Product.objects.all()
    context={
        'q':obj
    }
    return render(request,'temp/adminnew.html',context)

def view_rating(request):
    obj=Rating.objects.all()
    context={
        'pp':obj
    }
    return render(request, 'temp/adminnew.html', context)


def update_product(request,idd):
    obj = Product.objects.get(p_id=idd)
    context = {
        'a': obj
    }
    if request.method=="POST":
        obj=Product.objects.get(p_id=idd)
        obj.p_name=request.POST.get('uname')
        obj.p_price=request.POST.get('price')
        # myfile = request.FILES['img']
        # fs = FileSystemStorage()
        # filename = fs.save(myfile.name, myfile)
        # obj.p_image = myfile.name
        obj.p_type=request.POST.get('type')
        obj.p_color=request.POST.get('color')
        obj.p_thickness=request.POST.get('thick')
        obj.p_pattern=request.POST.get('pat')
        obj.save()
        return ppppp(request)
    return render(request, 'temp/update.html', context)


