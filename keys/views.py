# Create your views here.
from django.shortcuts import render

def home(request):
    return render(request, 'basic.html', {})
    
def cmd(request, cmd):
    print cmd
    return render(request, 'basic.html', {})