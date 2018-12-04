# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Issue(models.Model):
  IssueTitle = models.CharField('IssueTitle', max_length=32)
  IssueDesc = models.CharField('IssueDesc', max_length=128) # Improve to rich text object
  Submitter = models.ForeignKey(User)
  Vote = models.IntegerField('Vote', blank=False, default=0)
  View = models.IntegerField('View', blank=False, default=0)
  Answer = models.IntegerField('Answer', blank=False, default=0)
  Tags = models.CharField('Tags', max_length=128)
  CreateTime = models.DateTimeField('CreateTime', null=False, auto_now_add=True)
  LastModifyTime = models.DateTimeField('LastModifyTime', null=True, auto_now=True)

  class Meta:
    db_table = 'f_issue'
    ordering = ['-id']
