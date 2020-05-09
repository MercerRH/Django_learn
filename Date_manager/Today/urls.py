from django.conf.urls import url
from Today import views

urlpatterns = [
    url(r'^$', views.Today),
    url(r'^ajax_check/$', views.ajax_check),
    url(r'^delete/(\d+)$', views.delete_event),
]
