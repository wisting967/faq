# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.models import User
from models import Issue
from rest_framework import viewsets
from serializers import IssueSerializer

# Create your views here.
class IssueViewSet(viewsets.ModelViewSet):
  """
  API endpoint that allows users to be viewed or edited.
  """
  queryset = Issue.objects.all().order_by('-CreateTime')
  serializer_class = IssueSerializer
