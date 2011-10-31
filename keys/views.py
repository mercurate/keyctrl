#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Create your views here.
from django.shortcuts import render

def home(request):
    return render(request, 'keys.html', {})
    
def click(request, keys):
    print keys
    return render(request, 'keys.html', {})