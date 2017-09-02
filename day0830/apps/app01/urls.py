#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'xurui'
__date__ = '2017/8/30 21:06'
from django.conf.urls import url
from django.contrib import admin
from apps.app01 import views

urlpatterns = [
    url(r'^index.html/', views.index),
]

