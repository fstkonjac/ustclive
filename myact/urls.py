
from django.urls import path,include
from . import views
from .views import uploadImg

urlpatterns = [
    path("",views.indexActs, name="indexacts"),
    path("add",views.addActs, name="addacts"),
    path("insert",views.insertActs, name="insertacts"),
    path("del/<int:uid>", views.delActs, name="delact"),
    path("edit/<int:uid>",views.editActs, name="editusers"),
    path("users/update",views.indexActs, name="updateusers"),
]