# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class UserInfo(models.Model):
    uname = models.CharField(max_length=20)
    upwd = models.CharField(max_length=40)
    uemail = models.CharField(max_length=30)
    uaddress = models.CharField(max_length=100,default='')
    uphone = models.CharField(max_length=11,default='')
    isDelete = models.BooleanField(default=False)
