from datetime import datetime
from email.policy import default
from tkinter import Image, PhotoImage, image_names

from django.db import models

# Create your models here.

class Activities(models.Model):
    topic = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    details = models.CharField(max_length=100)
#上传图片和图片名字
    image = models.ImageField(upload_to='media',default='fuckyou.jpg')
    image_name=models.CharField(max_length=100)
#
    addtime = models.DateTimeField(default=datetime.now)
    creator = models.IntegerField(default=0)

    def toDict(self):
        return {'id':self.id,'username':self.username,'nickname':self.nickname,'password_hash':self.password_hash,'password_salt':self.password_salt,'status':self.status,'create_at':self.create_at.strftime('%Y-%m-%d %H:%M:%S'),'update_at':self.update_at.strftime('%Y-%m-%d %H:%M:%S')}

    class Meta:
        db_table = "activities"  # 更改表名
    