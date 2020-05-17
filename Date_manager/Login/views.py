from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from Login.models import User
from django.db.models import Q
import sys
import json


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
        userid = request.POST.get("input_userid")
        password = request.POST.get("input_pwd")
        u = User.objects.filter(Q(id__exact=userid) & Q(user_password__exact=password))  # 判断id与密码是否存在
        if not u:
            return JsonResponse({'res': '0'})  # 登录失败返回0
        else:
            data = {'res': '1'}
            # response = HttpResponse(json.dumps(data), content_type="application/json")
            response = JsonResponse(data)
            response.set_signed_cookie('user_id', userid, salt='test')  # 设置加密cookie
            return response


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
