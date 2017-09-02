from django.db import models


class UserType(models.Model):
    nid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=32)

class UserInfo(models.Model):
    """
    用户表
    """
    nid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=16)
    age = models.IntegerField()
    ut = models.ForeignKey('UserType')

