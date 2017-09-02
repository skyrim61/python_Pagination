from django.test import TestCase
from app03.models import  models
# Create your tests here.

res = models.UserInfo.objects.all()
print(res)