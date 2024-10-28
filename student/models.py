from django.db import models


class StudentProfile(models.Model):
    s_num = models.CharField(max_length=30, unique=True, primary_key=True)
    s_name = models.CharField(max_length=64)
    s_password = models.CharField(max_length=128)
    s_mail = models.CharField(max_length=64, null=True)
    s_class = models.CharField(max_length=64)
    s_flag = models.BooleanField(default=True)