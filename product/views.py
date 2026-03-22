from django.shortcuts import render
from product.models import Product
from django.core.files.storage import FileSystemStorage
from product.models import Cart
from product.models import Rating
# Create your views here.

def product(request):
    if request.method=="POST":
        obj=Product()
        obj.p_name=request.POST.get('uname')
        obj.p_price=request.POST.get('price')
        myfile = request.FILES['img']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        obj.p_image = myfile.name
        obj.p_type=request.POST.get('type')
        obj.p_color=request.POST.get('color')
        obj.p_thickness=request.POST.get('thick')
        obj.p_pattern=request.POST.get('pat')
        obj.save()
    return render(request,'product/product.html')

def view_product(request):
    obj=Product.objects.all()
    context={
        'a':obj
    }
    return render(request,'product/view_product.html',context)

def view_product_user(request):
    obj=Product.objects.all()
    context={
        'a':obj
    }
    return render(request,'product/pro.html',context)


def add_to_cart(request, idd):
    ss = request.session["u_id"]
    if request.method=="POST":
        obj=Cart()
        obj.qty=request.POST.get('qnty')
        obj.u_id=ss
        obj.p_id=idd
        obj.save()
    return render(request,'product/qty.html')

def view_cart(request):
    ss = request.session["u_id"]
    obj=Cart.objects.filter(u_id=ss)
    context={
        'a':obj
    }
    return render(request,'product/view_cart.html',context)

def remove(request,idd):
    obj=Cart.objects.get(cart_id=idd)
    obj.delete()
    return view_cart(request)

def rating(request,idd):
    ss = request.session["u_id"]
    if request.method=='POST':
        obj=Rating()
        obj.u_id=ss
        obj.p_id=idd
        obj.rating=request.POST.get('rating')
        obj.save()
    return render(request,'product/rating.html')

def view_rating(request):
    obj=Rating.objects.all()
    context={
        'x':obj
    }
    return render(request,'product/view_rating.html',context)


