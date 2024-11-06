from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # 新しいフィールドを追加
    student_id = models.CharField(max_length=32, unique=True)
    
    class Role(models.IntegerChoices):
        STUDENT = 0
        TEACHER = 1
        ADMIN = 2
    # user_permissionsフィールドの修正
    is_staff = models.BooleanField(default=False)  # 管理画面へのアクセス権
    user_permissions = models.ManyToManyField(
        'auth.Permission', 
        blank=True, 
        related_name="customuser_permissions"
    )
    
    # 新しいロールフィールド
    role = models.PositiveIntegerField(choices=Role.choices, default=Role.STUDENT)
    
    # 在籍フラグ
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.username  # 例: ユーザー名を返す
