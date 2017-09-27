# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponseRedirect, HttpResponse, redirect

# Create your views here.
def index(request):
    #start the journey
    return render(request, 'dashboard/index.html')