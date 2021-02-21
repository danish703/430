from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def signup(request):
    if request.method=='GET':
        return render(request,'signup.html')
    else:
        u = request.POST['username']
        e = request.POST['email']
        p1  = request.POST['pass1']
        p2 = request.POST['pass2']
        if p1==p2:
            user = User(username=u,email=e)
            user.set_password(p1)
            user.save()
            return redirect('signin')
        else:
            print("error aayo")
            print("password match vayena")


def signin(reqeust):
    if reqeust.method=='GET':
        return render(reqeust,'login.html')
    else:
        u = reqeust.POST['username']
        p = reqeust.POST['pass']

        user = authenticate(username=u,password=p)
        print(user)
        if user is not None:
            login(reqeust,user)
            return redirect('dash')
        else:
            print("tero password milena")
            return redirect('signin')

def dash(request):
    if request.user.is_authenticated:
        return render(request,'dashboard.html')
    else:
        return redirect('signin')


def signout(request):
    logout(request)
    return redirect('signin')