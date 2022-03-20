from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Goods(models.Model):
    NAME_MAX_LENGTH = 128
    name = models.CharField(max_length=NAME_MAX_LENGTH, unique=True)
    number = models.IntegerField(default=10)
    likes_num = models.IntegerField(default=0)
    # 保存的目录./media/image, 调用目录/static/media/image
    picture = models.ImageField(verbose_name='icon', null=False, blank=True, upload_to='image', max_length=200)
    price = models.IntegerField(default=10)

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    NAME_MAX_LENGTH = 128
    name = models.CharField(max_length=NAME_MAX_LENGTH, unique=True)
    password = models.CharField(max_length=NAME_MAX_LENGTH)
    email = models.CharField(max_length=128)
    money = models.IntegerField(default=10000)

    # toString
    def __str__(self):
        return self.user.username


class Likes(models.Model):
    likes_from = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    likes_to = models.ForeignKey(Goods, on_delete=models.CASCADE)
    create_time = models.DateTimeField(auto_created=True)
