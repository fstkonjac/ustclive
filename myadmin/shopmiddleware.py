# 自定义中间件类（执行是否登录判断）
from django.shortcuts import redirect
from django.urls import reverse
import re

class ShopMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print("ShopMiddleware")

    def __call__(self, request):
        path = request.path
        print("url:",path)

        # 判断管理后台是否登录
        # 定义不登录后台也可直接访问的url列表
        urllist = ['/myadmin/login','/myadmin/dologin','/myadmin/logout','/myadmin/verify']
        # 判断请求地址是否以/myadmin开头，且不在urllist中
        if re.match(r'^/myadmin',path) and (path not in urllist):
        #if (path not in urllist):
            # 判断是否登录(session中有无adminuser)
            if 'adminuser' not in request.session:
                # 重定向到登录页
                return redirect(reverse('myadmin_login'))

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response