from django.conf.urls import url
from Login import views

app_name = 'Login'

urlpatterns = [
    url(r'^$', views.index),
    url(r'^login/$', views.login, name='login'),
    url(r'^login_check/$', views.login_check),
    url(r'^register/$', views.register, name='register'),
]
