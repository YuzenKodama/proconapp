from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # 新しいフィールドを追加
    student_id = models.CharField(max_length=32, unique=True)
    class Role(models.IntegerChoices):
        STUDENT = 0
        TEACHER = 1
        ADMIN = 2
    first_name = None
    last_name = None
    date_joined = None
    groups = None
    last_login = None
    user_permissions = None
    role = models.PositiveIntegerField(choices=Role.choices, default=Role.STUDENT)
    is_active = models.BooleanField(default=True)  # 在籍フラグ
