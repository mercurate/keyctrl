#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'keys.html', {})
    
def cmd(request, args):
    print args
    return HttpRequest('')