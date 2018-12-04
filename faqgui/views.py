# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
import sys
import logging

if sys.getdefaultencoding() != 'utf-8':
  reload(sys)
  sys.setdefaultencoding('utf-8')

logger = logging.getLogger('swallowN')

# Create your views here.
def index(request):
  context = {}
  return render(request, 'faqindex.html', context)
