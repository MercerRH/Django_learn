from django.shortcuts import render, redirect
from django.http import JsonResponse
from Login.models import User
import sys


# Create your views here.

def index(request):
    """显示主页"""
    return render(request, 'index/index.html')


def login(request):
    """显示登录界面"""
    if request.method == 'POST':
        u = User()
        u.user_name = request.POST.get('username')
        u.user_password = request.POST.get('password')
        print(u.user_name, u.user_password)
        return redirect("/today/")
    else:
        return render(request, 'index/login.html')


def login_check(request):
    """检查登录"""
    if request.method == "POST":
        username = request.POST.get("input_username")
        password = request.POST.get("input_pwd")
        try:
            u = User.objects.get(user_name=username)
        except:
            print(sys.exc_info())  # 打印异常信息
            return JsonResponse({'res': '0'})  # 出现异常则失败返回0
        else:
            return JsonResponse({'res': '1'})  # 未出现异常则返回1


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        u = User()
        u.user_name = username
        u.user_password = password
        u.save()
        u_id = u.id
        return JsonResponse({'res': '1', 'uid': u_id})
    return render(request, 'index/register.html')
