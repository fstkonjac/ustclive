from datetime import datetime

from django.db import models

# Create your models here.

class Activities(models.Model):
    topic = models.CharField(max_length=32)
    name = models.CharField(max_length=32)
    phone = models.IntegerField(default=20)
    details = models.CharField(max_length=32)
    img_url = models.ImageField(upload_to='img',default="")
    addtime = models.DateTimeField(default=datetime.now)
    creator = models.IntegerField(default=0)

    def toDict(self):
        return {'id':self.id,'username':self.username,'nickname':self.nickname,'password_hash':self.password_hash,'password_salt':self.password_salt,'status':self.status,'create_at':self.create_at.strftime('%Y-%m-%d %H:%M:%S'),'update_at':self.update_at.strftime('%Y-%m-%d %H:%M:%S')}

    class Meta:
        db_table = "activities"  # 更改表名
    pic = models.ImageField(upload_to='pic/', verbose_name=u'图片地址')