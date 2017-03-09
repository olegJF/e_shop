# -*- coding: utf-8 -*-

from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', CategoryListAPIView.as_view(), name='home-api'),
    #url(r'^photo/$', PhototListAPIView.as_view(), name='photo-api'),
    url(r'^product/(?P<pk>\d+)/$', ProductDetailAPIView.as_view(), name='product-api'),
    url(r'^category/(?P<slug>[-\w]+)/$', CategoryDetailAPIView.as_view(), name='category-api'),
]
