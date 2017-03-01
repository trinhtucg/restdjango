from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^stock_list/', views.stock_list, name='stock_list'),
    url(r'^stock/', views.StockAPI.as_view())
]