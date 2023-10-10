from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from encrypted_fields import fields
# Create your models here.

class User1(AbstractBaseUser):
    """
        유저 프로필 사진
        유저 아이디    -> 화면에 표기되는 이름
        유저 이름      -> 실제 사용자 이름
        유저 이메일주소 -> 회원가입때 사용
        유저 비밀번호   -> 디폴트
    """
    profile_image = models.TextField()  # 프로필 이미지
    nickname = models.CharField(max_length=24, unique=True)
    name = models.CharField(max_length=24)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255, null=False, default=False)

    class Meta:
         db_table = "User1"
