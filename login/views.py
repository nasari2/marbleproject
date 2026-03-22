from django.shortcuts import render
from login.models import Login
from django.shortcuts import HttpResponseRedirect

# Create your views here.

def login(request):
    if request.method=='POST':
        username=request.POST.get("uname")
        password=request.POST.get("psw")
        obj=Login.objects.filter(username=username,password=password)
        tp=""
        for ob in obj:
            tp=ob.type
            uid=ob.u_id
            if tp=="admin":
                request.session["u_id"]=uid
                return HttpResponseRedirect('/temp/admin/')
            elif tp=="user":
                request.session["u_id"] = uid
                return HttpResponseRedirect('/temp/user/')
            elif tp=="delivery_boy":
                request.session["u_id"] = uid
                return HttpResponseRedirect('/temp/delivery_boy/')
        else:
            objlist="username or password incorrect...please try again...!"
            context={
                'msg':objlist
            }
            return render(request,'login/login.html',context)
    return render(request,'login/login.html')






# from django.shortcuts import render, redirect
# from django.contrib import messages
# from login.models import Login
#
#
# def login(request):
#     if request.method == 'POST':
#         username = request.POST.get("uname")
#         password = request.POST.get("psw")
#
#         # Look for a matching user in the Login table
#         obj = Login.objects.filter(username=username, password=password).first()  # Use .first() to get a single result
#
#         if obj:  # If the user is found
#             tp = obj.type
#             uid = obj.u_id
#
#             # Set the session variable
#             request.session["u_id"] = uid
#
#             # Redirect based on user type
#             if tp == "admin":
#                 return redirect('/temp/admin/')
#             elif tp == "user":
#                 return redirect('/temp/user/')
#             elif tp == "delivery_boy":
#                 return redirect('/temp/delivery_boy/')
#         else:
#             # If no match found, show error message
#             messages.error(request, "Username or password incorrect... please try again.")
#
#             # Re-render the login page with the error message
#             return redirect('login')  # Redirect to the login page to avoid re-submission of the form
#
#     # GET request: Render the login page
#     return render(request, 'login/login.html')
#
