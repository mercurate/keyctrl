#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

import os, sys, tempfile
#~ from SendKeys import SendKeys

KEY_MAP = {'left': '{LEFT}',
           'right': '{RIGHT}',
           'up': '{UP}',
           'down': '{DOWN}',
           'space': '{SPACE}',
           'enter': '{ENTER}',
           'shutdown': "{LWIN}rshutdown{SPACE}-s{SPACE}-t{SPACE}1{ENTER}"
          }

def home(request):
    Fn = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    return render(request, 'main2.html', {'Fn': Fn})
    
def cmd(request):
    c = request.GET['c']
    print c
    #~ SendKeys(KEY_MAP[c])
    return HttpResponse('')
