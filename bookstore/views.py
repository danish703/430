from django.shortcuts import HttpResponse,render

def home(request):
    return render(request,"index.html")

def contactus(request):
    return render(request,"contactus.html")

def aboutus(request):
    return render(request,"about.html")

def hello(request):
    return render(request,"hello.html")