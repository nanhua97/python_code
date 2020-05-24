from django.db import models
from tinymce.models import HTMLField
class UserInfo(models.Model):
    uname = models.CharField(max_length=20)
class BookInfo(models.Model):
    btitle = models.CharField(max_length=20)
    bpub_date = models.DateTimeField(db_column='pub_date')
    bread = models.IntegerField(default=0)
    bcommet = models.IntegerField(default=0)
    isDelete = models.BooleanField(default=False)
    class Meta:
        db_table = 'bookinfo'
class HeroInfo(models.Model):
    hname = models.CharField(max_length=10)
    hgender = models.BooleanField(default=False)
    hcontent = models.CharField(max_length=1000)
    isDelete = models.BooleanField(default=False)
    book = models.ForeignKey(BookInfo)

class Areas(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=20)
    parea = models.ForeignKey('Areas',null=True,blank=True)
# Create your models here.

class Test(models.Model):
    content = HTMLField()
    def __str__(self):
        return self.content
