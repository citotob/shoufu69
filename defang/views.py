# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

#@login_required
def home(request):
    return render(request, 'index.html')
    #return HttpResponse("Hello, world. You're at the helthnews index.")

def signin(request):
    return render(request, 'login.html')

#def home(request):
#    username = None
#    if request.user.is_staff:
#       return redirect('/admin/')
#    else:
#       return render(request, 'index.html',{})
