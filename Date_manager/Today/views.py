from django.shortcuts import render
from django.http import JsonResponse
# from Login.models import User
from Today.models import Event
from Login.models import User
from Date_manager.login_cookie_check import is_login


# Create your views here.
@is_login
def Today(request):
    context = {}
    uid = request.get_signed_cookie('user_id', salt='test')
    context['all'] = Event.objects.filter(user_id=uid)
    context['user_head'] = User.objects.get(id=uid)
    return render(request, 'Today/today.html', context)


@is_login
def ajax_check(request):
    # 获取返回的数据
    if request.method == "POST":  # 判断是否收到POST提交
        input_title = request.POST.get('input_title')
        input_content = request.POST.get('input_content')
        start_time = request.POST.get('start_time')
        end_time = request.POST.get('end_time')

        # 获取cookie中的用户id
        u_id = request.get_signed_cookie('user_id', salt='test')
        # 往数据库内写入数据
        event = Event()
        event.title = input_title
        event.content = input_content
        event.start_time = start_time
        event.end_time = end_time
        event.user_id_id = u_id
        event.save()

    return JsonResponse({})


@is_login
def delete_event(request, e_id):
    event = Event.objects.get(id=e_id)
    event.delete()
    return JsonResponse({})


@is_login
def my(request):
    u_id = request.get_signed_cookie("user_id", salt="test")
    user_name = User.objects.get(id=u_id)
    context = {}
    context["user_name"] = user_name
    return render(request, 'Today/my.html', context)


@is_login
def all_event(request):
    """在所有事件界面显示每一年的列表"""
    context = {}
    uid = request.get_signed_cookie("user_id", salt="test")
    all_event = Event.objects.filter(user_id=uid)
    context['all_event'] = all_event
    return render(request, 'Today/all_event.html', context)
