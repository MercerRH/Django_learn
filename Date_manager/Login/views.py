from django.shortcuts import render, redirect
from Login.models import User


# Create your views here.

def index(request):
    """显示主页"""
    return render(request, 'index/index.html')


def login(request):
    """显示登录界面"""
    if request != None:
        u = User()
        u.user_name = request.POST.get('username')
        u.user_password = request.POST.get('password')
        print(u.user_name, u.user_password)
        return redirect("/today/")
    else:
        return "error"