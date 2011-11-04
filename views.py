#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

import os, sys, string, tempfile
from SendKeys import SendKeys

CMD_MAP = {
           'standby':  "{LWIN}us",
           'shutdown': "{LWIN}uu",
           'restart':  "{LWIN}ur",
          }

def home(request):
    A = string.ascii_uppercase
    N = range(1,13)
    return render(request, 'keys.html', {'N': N, 'A': A})
    
def key(request):
    key = request.GET['key']
    ctrl = request.GET['ctrl']
    alt = request.GET['alt']
    shift = request.GET['shift']
    
    key = '{%s}' % key
    
    if ctrl == 'true':
        print 'ctrl'
        key = '^' + key

    if alt == 'true':
        print 'alt'        
        key = '%' + key
        
    if shift == 'true':
        print 'shift'        
        key = '+' + key
        
    SendKeys(key, pause = 0.5)
    print key
    return HttpResponse('')
        
def cmd(request):
    c = request.GET['cmd']
    SendKeys(CMD_MAP[c], pause = 0.01)
    print c
    return HttpResponse('')     
