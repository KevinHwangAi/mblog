from django.db import models
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=200) #文章标题
    slug = models.CharField(max_length=200) #文章网址
    body = models.TextField() #文章内容
    pub_date = models.DateTimeField(default=timezone.now) #发文时间

    class Meta:
        ordering = ('-pub_date',)

        def __unicode__(self):
            return title


