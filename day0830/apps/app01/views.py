from django.shortcuts import render, HttpResponse, redirect
from apps.app01 import models

# Create your views here.


from apps.utils.pager import PageInfo


def index(request):
    # for i in range(300):
    #     name = "root" + str(i)
    #     models.UserInfo.objects.create(name=name, age=18, ut_id=1)
    # return HttpResponse(1111)
    # user_list=models.UserInfo.objects.all()
    # all_count = models.UserInfo.objects.all().count()
    all_count = models.UserInfo.objects.all().count()
    page_info = PageInfo(request.GET.get('page'), all_count, '/app01/index.html/')
    user_list = models.UserInfo.objects.all()[page_info.start():page_info.end()]
    return render(request, 'custom.html', {"user_list": user_list, "page_info": page_info})
