"""用于验证登录状态的装饰器"""
from django.shortcuts import redirect
from django.core.urlresolvers import reverse


def is_login(func):
    def function(request, *args, **kwargs):
        u_name = request.COOKIES.get('user_id')
        if u_name:
            return func(request, *args, **kwargs)
        else:
            # # 获取用户当前访问的url，并传递给/login/
            # next = request.get_full_path()
            return redirect(reverse('Login:login'))
    return function
