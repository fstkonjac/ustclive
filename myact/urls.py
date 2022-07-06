
from django.urls import path,include
from . import views
from . import act

urlpatterns = [
    path("",views.index, name="myact_index"),
    path("act/add",act.add, name="myact_act_add"),
    path("act/insert",act.insert, name="myact_act_insert"),
    path("act/delete/<int:uid>", act.delete, name="myact_act_delete"),
    path("act/edit/<int:uid>",act.edit, name="myact_act_edit"),
    path("act/detail/<int:uid>",act.detail, name="myact_act_detail"),
    path("act/update/<int:uid>",act.update, name="myact_act_update"),
    path('act/<int:pIndex>', act.index, name='myact_act_index'), # 浏览
]