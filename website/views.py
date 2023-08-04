from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'index.html',{})


def product(request):
    return render(request,'product.html',{})
def viewProduct(request):
    return render(request,'viewproduct.html',{})


def aboutus(request):
    return render(request,'aboutus.html',{})


def contactus(request):
    return render(request,'contactus.html',{})







def orders(request):
    return render(request,'orders.html',{})

def checkout(request):
    return render(request,"checkout.html",{})

def signIn(request):
    return render(request,'signin.html',{})

def signUp(request):
    return render(request,"signup.html",{})








def base(request):
    return render(request,'base.html',{})