# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 17:25:28 2016

@author: TimRe
"""

from django.conf.urls import url

from . import views

urlpatterns=[url(r'^$', views.post_list, name='post_list'),]
