from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login ,logout
from datetime import datetime
from home.models import Fruits
from .forms import NameForm

# Create your views here.




def index(request):

   fruits=Fruits.objects.all()
   context={'fruits' : fruits}
   # if request.user.is_anonymous :
   #    redirect('/login')
   return render(request,'index.html',context)
def about(request):
   return render(request,'about.html')


def add(request) :
  error ={
         'message' : "Please Login"
      }
  if request.method=="POST" :
   name = request.POST.get('name')
   price = request.POST.get('price')
   qty = request.POST.get('qty')
   fruits = Fruits(name=name,price=price,qty=qty)
   fruits.save()
   return redirect('add')
  else :
   if not request.user.is_anonymous :
      return render(request,'add.html')
   else :
      return render(request,'error.html',error)
   
def update(request,id) :
   error ={
         'message' : "Please Login"
    }
   if not request.user.is_anonymous :
      fruit=Fruits.objects.get(id=id)
     
      context ={
      'fruit' : fruit
      }
     
      if request.method=='POST' :
      
         fruit.name=request.POST.get('name')
         fruit.price=request.POST.get('price')
         fruit.qty=request.POST.get('qty')
         fruit.save()

         # if form.is_valid() :
         #    form.save()

         return redirect(index)
      
      return render(request,'update.html',context)
   
   else :
      return render(request,'error.html',error)

def delete(request,id) :
   if not request.user.is_anonymous :
      fruit = Fruits.objects.get(id=id)
      fruit.delete()
      return redirect(index)
   return render(request,'error.html')

def login(request):
   error ={
         'message' : "Incorrect Credentials!!"
      }
   if request.method=='POST' :
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None:
           auth_login(request,user)
           return redirect('/')
        else :
           return render(request,'error.html',error)
      #   login = Login(email=email,password=password)
      #   login.save()
   # elif request.user is not none :
   #      return redirect('/')

   return render(request,'login.html')

def register(request) :
   if request.method=='POST' :
      username = request.POST.get('username')
      email = request.POST.get('email')
      password = request.POST.get('password')
      user = User.objects.create_user(username,email,password)
      user.save()
      return redirect('/login')
   else :
      return render(request,'register.html')

def logoutUser(request) :
   logout(request)
   return redirect('/login')

def buy(request,id) :
   fruit = Fruits.objects.get(id=id)
   if request.method=="POST" :
      purchaseQty=request.POST.get("Qty")
      print(purchaseQty)
      remainFruits=int(fruit.qty)-int(purchaseQty)
      fruit.qty=remainFruits
      fruit.save()
      return redirect('/')
   context = {
      'fruit' : fruit
   }

   return render(request,'buy.html',context)