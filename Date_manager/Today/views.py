from django.shortcuts import render
from Today.models import Event


# Create your views here.

def Today(request):
    context = {}
    context['all'] = Event.objects.all()
    return render(request, 'Today/today.html', context)


def add(request):
    return render(request, 'Today/add.html')
