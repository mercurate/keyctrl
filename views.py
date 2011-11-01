#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'main.html', {})
    
def cmd(request):
    c = request.GET['c']
    print c
    return HttpResponse('')
