from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from Today.models import Event


# Create your views here.

def Today(request):

    context = {}
    context['all'] = Event.objects.all()
    return render(request, 'Today/today.html', context)


def ajax_check(request):
    # 获取返回的数据
    if request.method == "POST":  # 判断是否收到POST提交
        input_title = request.POST.get('input_title')
        input_content = request.POST.get('input_content')
        start_time = request.POST.get('start_time')
        end_time = request.POST.get('end_time')

        # 往数据库内写入数据
        event = Event()
        event.title = input_title
        event.content = input_content
        event.start_time = start_time
        event.end_time = end_time
        event.save()

    return JsonResponse({})


def delete_event(request, e_id):
    event = Event.objects.get(id=e_id)
    event.delete()
    return JsonResponse({})

