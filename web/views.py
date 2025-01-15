from django.shortcuts import render,redirect,get_object_or_404
from .forms import *
from .models import * 
from django.contrib.auth import authenticate,login,logout
from .models import Vendor 
from .forms import Packageform 
from django.contrib.auth.decorators import login_required




# Create your views here.
@login_required
def home(request):
    return render(request,"home.html")
def index(request):
    return render(request,"index.html")
def register(request):
    if request.method =='POST':
        form= UserReistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            raw_password = form.cleaned_data.get('password1')
            user.set_password(raw_password)
            user.save()
            return redirect('login')
    else:
        form=UserReistrationForm()
    return render(request,"register.html",{'form':form})
    
def Userlogin(request):
    if request.method=='POST':
        form=Userloginform(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request, user)
                return redirect('userdash')
    else:
        form=Userloginform
    return render(request,"login.html",{'form':form})

def Package_data(request):
    if request.method == 'POST':
        form =Packageform(request.POST,request.FILES)
        if form.is_valid():
            Package=form.save(commit=False)
            Package.is_approved = False
            Package.save()
            return redirect('dash')
    else:
        form=Packageform()
    return render(request,"package.html",{'form':form})
    
def vendor_reg(request):
    if request.method == 'POST':
        form =Vendorform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vendor_login')
    else:
        form=Vendorform()
    return render(request,"vendorreg.html",{'form':form})

def vendor_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            try:
                vendor = Vendor.objects.get(username=username, password=password)
                return redirect('dash') 
            except Vendor.DoesNotExist:
                form.add_error(None, "Invalid username or password")
    else:
        form = LoginForm()
    
    return render(request, "vendorlog.html", {"form": form})
 
def dash(request):
    datas=Package.objects.all()
    return render(request,"dash.html",{'item':datas})

@login_required
def payment(request):
    return render(request,"payment.html")
def delt(request,pk):
    datas=get_object_or_404(Package,pk=pk)
    if request.method == 'POST':
        datas.delete()
        return redirect('dash')
def edited(request,pk):
    datas=get_object_or_404(Package,pk=pk)
    if request.method == 'POST':
        form=Packageform(request.POST,instance=datas)
        if form.is_valid():
            form.save()
            return redirect('dash')
    else:
        form=Packageform(instance=datas)
    return render(request,"update.html",{'form':form})

def Package_data1(request):
    if request.method == 'POST':
        form =Packageform(request.POST,request.FILES)
        if form.is_valid():
            Package=form.save(commit=False)
            Package.is_approved = False
            Package.save()
            return redirect('user_dash')
    else:
        form=Packageform()
    return render(request,"package.html",{'form':form})
def user_dash(request):
    datas=Package.objects.all()
    return render(request,"userdash.html",{'item':datas})

@login_required
def uslogout(request):
    logout(request)
    return redirect('index')
    







 






    







            

