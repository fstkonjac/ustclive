# 员工信息视图文件
from django.shortcuts import render
from django.http import HttpResponse
from grpc import Status
from myact.models import Activities
from django.core.paginator import Paginator
from django.db.models import Q
from datetime import datetime
# Create your views here.

def index(request,pIndex=1):
    '''浏览信息'''
    Umod = Activities.objects
    alist = Umod.filter(creator__exact=request.session['generaluser']['id'])
    mywhere = []
    # 获取并判断搜索条件
    kw = request.GET.get('keyword',None)
    if kw:
        alist = alist.filter(Q(name__contains=kw) | Q(creator__contains=kw))
        mywhere.append('keyword='+kw)
    # 获取、判断并封装状态status搜索条件
    # status = request.GET.get('status','')
    # if status != '':
    #     list = list.filter(status=status)
    #     mywhere.append("status="+status)
    # 执行分页
    pIndex = int(pIndex)
    page = Paginator(alist,15) # 以每页15条数据分页
    maxpages = page.num_pages # 获取最大页数
    # 判断当前页是否越界
    if pIndex > maxpages:
        pIndex = maxpages
    if pIndex < 1:
        pIndex = 1
    list2 = page.page(pIndex) # 获取当前页数据
    plist = page.page_range # 获取页码列表信息
    context ={'actlist':list2,'plist':plist,'pIndex':pIndex,'maxpages':maxpages,'mywhere':mywhere}
    return render(request,"myact/act/index.html",context)

# 加载活动添加表单
def add(request):
    ''' img_name = ''
    if request.method == 'POST':
        img_obj = request.FILES['img']  # 获取上传文件对象
        img_name = request.FILES['img'].name  # 获取上传文件的字符串类型名称
        path = 'static/' + img_name
        with open(path, mode='wb') as f:
            for content in img_obj.chunks():  # 读取上传文件的内容
                f.write(content)    # 存储图像文件'''
    return render(request,"myact/act/add.html")
# 执行活动添加
def insert(request):
    if request.method == 'POST':
        new_message = Activities(
            name = request.POST.get('name'),
            topic = request.POST.get('topic'),
            phone = request.POST.get('phone'),
            details = request.POST.get('details'),
            creator = request.session['generaluser']['id'],

            # image=request.FILES.get('photo'),
            # image_name=request.FILES.get('photo').name

        )
        new_message.save()
        context = {"info": "添加成功！"}
        return render(request,"myact/act/info.html",context)

def delete(request,uid=0):
    '''执行信息删除'''
    try:
        ob = Activities.objects.get(id=uid)
        ob.delete()
        context = {'info':"删除成功！"}
    except Exception as err:
        print(err)
        context = {'info':"删除失败！"}
    return render(request,"myact/act/info.html",context)

def edit(request,uid=0):
    '''加载信息编辑表单'''
    try:
        ob = Activities.objects.get(id=uid)
        context = {'act':ob}
        return render(request,"myact/act/edit.html",context)
    except Exception as err:
        print(err)
        context = {'info':"没有找到要修改的信息！"}
    return render(request,"myact/act/info.html",context)

def detail(request,uid=0):
    ob = Activities.objects.get(id=uid)
    context = {'act':ob}
    return render(request,"myact/act/detail.html",context)

def update(request,uid=0):
    '''执行信息编辑'''
    try:
        ob = Activities.objects.get(id=uid)
        ob.name = request.POST['name'],
        ob.topic = request.POST['topic'],
        ob.phone = request.POST['phone'],
        ob.details = request.POST['details'],
        ob.save()
        context = {'info':"修改成功！"}
    except Exception as err:
        print(err)
        context = {'info':"修改失败！"}
    return render(request,"myact/act/info.html",context)
