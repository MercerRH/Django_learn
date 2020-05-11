from django.shortcuts import render


# Create your views here.

def index(request):
    """显示主页"""
    return render(request, 'index/index.html')


def login(request):
    """显示登录界面"""
    return render(request, 'index/login.html')