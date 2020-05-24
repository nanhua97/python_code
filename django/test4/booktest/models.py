from django.db import models

class BookInfo(models.Model):
    btitle = models.CharField(max_length = 20)
    bpub_date = models.DateTimeField(db_column = 'pub_date')
    bread = models.IntegerField(default=0)
    bcommet = models.IntegerField(default=0)
    isDelete = models.BooleanField(default = False)
    class Meta:
        db_table = 'bookinfo'
class HeroInfo(models.Model):
    hname = models.CharField(max_length=10)
    hgender = models.BooleanField(default = False)
    hcontent = models.CharField(max_length=1000)
    isDelete = models.BooleanField(default = False)
    book = models.ForeignKey(BookInfo)
    def showname(self):
        return self.hname
# Create your models here.
