# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

def index(request):
	return render(request,'webapp/home.html')

def contact(request):
	return render(request, 'webapp/contact.html', {'content':['Contact me','pabasara.uom@gmail.com']})


def page2(request):
	return render(request,'webapp/page2.html',{'content':['Contact me','pabasara.uom@gmail.com']})
# Create your views here.
