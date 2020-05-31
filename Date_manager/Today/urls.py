from django.conf.urls import url
from Today import views

app_name = 'Today'

urlpatterns = [
    url(r'^$', views.Today, name='today'),
    url(r'^ajax_check/$', views.ajax_check),
    url(r'^delete/(\d+)$', views.delete_event),
    url(r'^my/$', views.my),
    url(r'^all_event/$', views.all_event)
]
