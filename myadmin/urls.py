# 后台管理子路由
from django.urls import path
from myadmin.views import index
from myadmin.views import user

urlpatterns = [
    path('', index.index, name='myadmin_index'), # 后台首页

    # 账号注册路由
    path('register', index.register, name='myadmin_register'),
    path('doregister', index.doregister, name='myadmin_doregister'),

    # 后台管理员登录、退出路由
    path('login', index.login, name='myadmin_login'), # 加载登录表单
    path('dologin', index.dologin, name='myadmin_dologin'), # 执行登录
    path('logout', index.logout, name='myadmin_logout'), # 退出
    path('verify', index.verify,name='myadmin_verify'), # 输出验证码

    # 员工信息管理路由
    path('user/<int:pIndex>', user.index, name='myadmin_user_index'), # 浏览
    path('user/add', user.add, name='myadmin_user_add'), # 添加表单
    path('user/insert', user.insert, name='myadmin_user_insert'), # 执行添加
    path('user/del/<int:uid>', user.delete, name='myadmin_user_delete'), # 执行删除
    path('user/edit/<int:uid>', user.edit, name='myadmin_user_edit'), # 添加编辑表单
    path('user/update/<int:uid>', user.update, name='myadmin_user_update'), # 执行编辑
]
