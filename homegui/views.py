# -*- coding: utf-8 -*-
 
#from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings
import json
import os
 
def index(request):
  context          = {}
  context['hello'] = 'Hello World!'
  menufile = open(os.path.join(settings.BASE_DIR, 'homegui/templates/menu.json'), 'r')
  context['menuList'] = json.loads(menufile.read())
  return render(request, 'index.html', context)
