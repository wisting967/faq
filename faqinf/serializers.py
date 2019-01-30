# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import serializers
from models import Issue
from django.contrib.auth.models import User
import logging

logger = logging.getLogger('swallowN')

class IssueSerializer(serializers.ModelSerializer):
  SubmitterID = serializers.IntegerField(source='Submitter.id', read_only=True)
  SubmitterName = serializers.CharField(source='Submitter.username', read_only=True)
  
  class Meta:
    model = Issue
    fields = ('id', 'IssueTitle', 'IssueDesc', 'SubmitterID', 'SubmitterName', 'Vote', 'View', 'Answer', 'Tags', 'CreateTime', 'LastModifyTime')
    #read_only_fields = ('CreateTime', 'LastModifyTime'), Not used, auto fields, foreign fields need specified explicitly

  def create(self, validated_data):
    logger.info('create')
    logger.info(validated_data)
    return Issue.objects.create(Submitter=User.objects.get(id=1), **validated_data)
