#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

import os, sys, tempfile
from SendKeys import SendKeys

KEY_MAP = {'left': '{LEFT}',
           'right': '{ROGHT}',
           'up': '{UP}',
           'down': '{DOWN}',
           'space': '{SPACE}',
           'enter': '{ENTER}',
           'shutdown': "{LWIN}rshutdown{SPACE}-s{SPACE}-t{SPACE}1{ENTER}"
          }

def home(request):
    return render(request, 'main.html', {})
    
def cmd(request):
    c = request.GET['c']
    print c
    SendKeys(KEY_MAP[c])
    return HttpResponse('')
