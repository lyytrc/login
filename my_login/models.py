from django.db import models
from django.utils import timezone

# Create your models here.
class User(models.Model):     # 引用Model类
    """ 用户表 """
    GENDER_CHOICE = (
        ('male','男') ,
        ('female','女'),
        ('unknown','未知'),
    )
    name = models.CharField('昵称',max_length=8)      #a最大长度
    password=models.CharField('密码',max_length=16)
    hash_password = models.CharField('哈希密码',max_length=128,null=True,blank=True)
    gender=models.CharField('性别',choices=GENDER_CHOICE,max_length=10,default=GENDER_CHOICE[2][0])# 选项choices   default默认值[2]下标2[1]下标1
    email = models.CharField('邮箱',max_length=100,unique=True)
    regiseter_time =models.DateTimeField('注册日期',default=timezone.now)# DATETIME时间专用      timezone需要调用。

