from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.hello, name='blog'),
    url(r'^testparam/(\d+)/', views.test_param, name='testparam'),
    url(r'^index', views.index, name='index')
]