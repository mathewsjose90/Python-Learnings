from django.conf.urls import url
from django.contrib import admin

from . import views

app_name = 'companies'

urlpatterns = [
    # /stocks
    url(r'^$', views.StockList.as_view(), name='stocklist'),

]
