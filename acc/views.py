from email import message
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.hashers import check_password
from django.contrib import messages

from acc.models import User

# Create your views here.
def index(request):
    return render(request,'acc/index.html')

def login_user(request):
    if request.method=="POST":
        un = request.POST.get("uname")
        up = request.POST.get("upass")
        user = authenticate(username=un, password=up)
        if user:
            login(request,user)
            messages.success(request,f"{user}님 환영합니다!")
            return redirect('acc:index')
        else:
            messages.error(request,"계정 정보가 일치하지 않습니다.")
    return render(request,'acc/login.html')

def logout_user(request):
    logout(request)
    return redirect("acc:index")

def signup(request):
    # print(request.POST)
    # print(request.FILES)
    if request.method=="POST":
        un = request.POST.get("uname")
        up = request.POST.get("upass")
        ua = request.POST.get("uage")
        uc = request.POST.get("ucom")
        pi = request.FILES.get("upic")
        print()
        try:
            User.objects.create_user(username=un,password=up,age=ua,comment=uc,pic=pi)
            return redirect('acc:login')
        except:
            messages.warning(request,"계정 등록에 실패하였습니다..")
        
    return render(request,'acc/signup.html')

def profile(request):
    return render(request,'acc/profile.html')

def update(request):
    if request.method=="POST":
        u = request.user
        up = request.POST.get("upass")
        ua = request.POST.get("uage")
        uc = request.POST.get("ucom")
        pi = request.FILES.get("upic")

        if up:
            u.set_password(up)
        u.comment=uc
        u.age = ua
        if pi :
            u.pic.delete()
            u.pic = pi
        u.save()
        login(request,u)
        return redirect("acc:profile")

def delete(request):
    u=request.user
    up = request.POST.get("pwck")
    if check_password(up,u.password):
        u.pic.delete()
        u.delete()
        return redirect("acc:index")
    else:
        messages.error(request,"비밀번호가 일치하지 않습니다!")
    return redirect("acc:profile")

