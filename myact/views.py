from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render
from myact.models import Activities


# Create your views here.
#def index(request):
    #ob =Users()
    #ob.name = "jj"
    #ob.phone = "110"
    #ob.detail="is super cleverpy
    #ob.save()
    # delete
    #mod =Users.objects
    #user=mod.get(id=3)
    #print(user.name)
   # mod=Users.objects
   # ulist=mod.all()
    #for u in ulist:
    #    print (u.name)

   # return HttpResponse("首页")
def index(request):
   # mod = Users2.all()
    #ulist = mod.order_by("id")  # 按age升序排序,只获取前3条
    #for u in ulist:

    return HttpResponse("首页 <br/> <a href='/activities/users'>用户信息管理</a>")
#浏览用户信息
def indexActs( request ):
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
def lishan02(request):
    img_name = ''
    if request.method == 'POST':
        img_obj = request.FILES['picture']  # 获取上传文件对象
        img_name = request.FILES['picture'].name  # 获取上传文件的字符串类型名称
        path = 'static/' + img_name
        with open(path, mode='wb') as f:
            for content in img_obj.chunks():  # 读取上传文件的内容
                f.write(content)    # 存储图像文件
    return render(request, 'app01/lishan02.html', {'image': img_name})

def addActs(request):
    ''' img_name = ''
    if request.method == 'POST':
        img_obj = request.FILES['img']  # 获取上传文件对象
        img_name = request.FILES['img'].name  # 获取上传文件的字符串类型名称
        path = 'static/' + img_name
        with open(path, mode='wb') as f:
            for content in img_obj.chunks():  # 读取上传文件的内容
                f.write(content)    # 存储图像文件'''
    return render(request,"myact/addAct.html")
#执行用户信息添加
def insertActs(request):
    #try:
        ob=Activities()
        ob.name = request.POST['name']
        ob.topic = request.POST['topic']
        ob.phone = request.POST['phone']
        print(3)
        ob.details = request.POST['detail']
        print(4)
        ob.img_url= request.POST['img']
        print(5)
        ob.save()  # 执行保存
        print(6)
        context = {"info": "添加成功！"}
    #except:
     #   context = {"info": "添加失败！"}
        return render(request,"myact/info.html",context)

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
def uploadImg(request):
    #if request.method=='POST':
    #    img=Img(img_url=request.FILES.get('img'))
    #    img.save()
    return render(request,'imgupload.html')
#会员登陆表单
