# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
import requests
import sys
import logging

if sys.getdefaultencoding() != 'utf-8':
  reload(sys)
  sys.setdefaultencoding('utf-8')

logger = logging.getLogger('swallowN')

# Create your views here.
def index(request):
  context = {}
  _session = requests.session()
  _res = _session.get('http://127.0.0.1:8080/faqapi/v1/issue/')
  if _res.status_code == requests.codes.ok:
    context['issueList'] = _res.json()
    logger.info(_res.json())
  return render(request, 'faqindex.html', context)

def new(request):
  context = {}
  _session = requests.session()
  return render(request, 'newfaq.html', context)
