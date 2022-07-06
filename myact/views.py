from datetime import datetime
from tkinter import image_names
from webbrowser import get

from django.http import HttpResponse
from django.shortcuts import render
from myact.models import Activities
from myact import models


# Create your views here.
from django.core.files.base import ContentFile

#浏览用户信息
def index( request ):
    try:
        ulist =Activities.objects.all()
        context={"userlists":ulist}
        print(ulist)
        return render(request,"myact/showall.html",context)
    except:
        return HttpResponse("no response")
    pass
#添加用户信息表单
#上传文件：
#上传文件：

#执行用户信息删除
def delActs(request,uid=0):
    try:
        ob = Activities.objects.get(id=uid)  # 获取要删除的数据
        ob.delete()  # 执行删除操作
        context = {"info": "删除成功！"}
    except:
        context = {"info": "删除失败！"}
    return render(request, "myact/info.html", context)
#加载用户信息表单
def editActs(request,uid=0):
    pass
#执行用户信息修改
def updateUsers(request):
    pass
