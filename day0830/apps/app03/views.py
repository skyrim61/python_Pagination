from django.shortcuts import render, HttpResponse, redirect
# Create your views here.
# from app03.models import models
# def index(request):
#     # for i in range(300):
#     #     name = "root" + str(i)
#     #     models.UserInfo.objects.create(name=name, age=18, ut_id=1)
#     user_list=models.UserInfo.objects.all()
#     # user_list=models.UserInfo.objects.all()
#     return HttpResponse(user_list)
#     return  render(request, 'index.html',{"user_list": user_list})