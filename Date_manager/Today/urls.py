from django.conf.urls import url
from Today import views

urlpatterns = [
    url(r'^$', views.Today),
    url(r'^add$', views.add),
]
