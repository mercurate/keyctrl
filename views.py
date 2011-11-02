#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

import os, sys, tempfile
from SendKeys import SendKeys

CMD_MAP = {
           'standby': "{LWIN}us",
           'shutdown': "{LWIN}uu",
           'restart': "{LWIN}ur",
          }

def home(request):
    Fn = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    return render(request, 'main2.html', {'Fn': Fn})
    
def key(request):
    try:
        k = request.GET['k']
        SendKeys(k, pause = 0.5)
        print k
        return HttpResponse('')
    except Exception, e:
        print e
        
def cmd(request):
    try:
        k = request.GET['k']
        SendKeys(CMD_MAP[k], pause = 0.5)
        print k
        return HttpResponse('')
    except Exception, e:
        print e        
