# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import serializers
from models import Issue
from django.contrib.auth.models import User

class IssueSerializer(serializers.ModelSerializer):
  #SubmitterID = serializers.IntegerField(source='User.id')
  #SubmitterName = serializers.CharField(source='User.last_name')
  
  class Meta:
    model = Issue
    #fields = ('id', 'IssueTitle', 'IssueDesc', 'SubmitterID', 'SubmitterName', 'Vote', 'View', 'Answer', 'Tags', 'CreateTime', 'LastModifyTime')
    fields = ('id', 'IssueTitle', 'IssueDesc', 'Vote', 'View', 'Answer', 'Tags', 'CreateTime', 'LastModifyTime')
