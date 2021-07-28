from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                related_name='profile')

    image = models.ImageField(upload_to='profile/', null=True)
    nickname = models.CharField(max_length=30, unique=True, null=True)
    message = models.CharField(max_length=200, null=True)
#on_delete 삭제됐을 때 할 행동을 설정, 삭제 정책 CASCADE 종속
#저장경로 설정 (profile폴더를 만들어서 거기에 이미지를 보관하겠다.)
#글자수30, 문자열 겹치지 않게