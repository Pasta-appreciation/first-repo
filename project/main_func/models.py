from django.db import models
from accounts.models import CustomUser
from pathlib import Path

# Create your models here.
#以下chatGPTに投げるためのPronpt
"""
ER図
#seniors table
PK: senior_id
created_at: datetime
updated_at: datetime
name
age
address
description :経歴や自己PR
face_path :プロフィール画像のパス
is_wanted ：募集中かどうか

#matchings Table
PK: matching_id
FK: senior_id
FK: job_id 
created_at: datetime
updated_at: datetime
state :1=応募者からの申請、2=企業からの申請、3=マッチング成立、4=マッチング不成立
matched_on :いつマッチングしたか（いつstateが3になったか）

#jobs table
PK: job_id
FK: company_id
created_at: datetime
updated_at: datetime
number_of_people :募集人数
description :仕事内容、応募資格など
is_public  :公開中の募集かどうか
is_deleted :削除された募集かどうか

#companies table
PK: company_id
created_at: datetime
updated_at: datetime
name
address
industry
homepage_url
pic_path :企業のロゴ画像のパス
description :企業の説明
"""
from django.db import models

class Senior(models.Model):
    senior_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)#users紐付け
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255) #default指定しなきゃ
    age = models.IntegerField(blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    face_path = models.ImageField(upload_to=Path('/images/senior_faces/'), blank=True, null=True)
    is_wanted = models.BooleanField(default=False)

class Company(models.Model):
    company_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)#users紐付け
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255,blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    industry = models.CharField(max_length=255,blank=True, null=True)
    homepage_url = models.URLField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    pic_path = models.ImageField(upload_to=Path('/images/company_pics/'), blank=True, null=True)

class Job(models.Model):
    job_id = models.AutoField(primary_key=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    number_of_people = models.IntegerField(default=0)
    description = models.TextField()
    is_public = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)

class Matching(models.Model):
    matching_id = models.AutoField(primary_key=True)
    senior = models.ForeignKey(Senior, on_delete=models.CASCADE)
    job_id = models.ForeignKey(Job, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    state = models.IntegerField() #1=応募者からの申請、2=企業からの申請、3=マッチング成立、4=マッチング不成立
    matched_on = models.DateTimeField(null=True, blank=True)