from django.db import models

# python manage.py inspectdb >booktest/models.py
class BookInfoManager(models.Manager):
    def get_queryset(self):
        return super(BookInfoManager,self).get_queryset().filter(isDelete=False)
    def create(cls,btitle,bpub_date):
        b = BookInfo()
        b.btitle = btitle
        b.bpub_date = bpub_date
        b.bread = 0
        b.bcommet = 0
        b.isDelete = False
        return b
class BookInfo(models.Model):
    btitle = models.CharField(max_length=20)
    bpub_date = models.DateTimeField(db_column='pub_date')
    bread = models.IntegerField(default=0)
    bcommet = models.IntegerField(default=0)
    isDelete = models.BooleanField(default=False)
    class Meta:
        db_table = 'bookinfo'
    books1 = models.Manager()
    books2 = BookInfoManager()

    @classmethod
    def create(cls,btitle,bpub_date):
        b = BookInfo()
        b.btitle = btitle
        b.bpub_date = bpub_date
        b.bread = 0
        b.bcommet = 0
        b.isDelete = False
        return b
    def __str__(self):
        return self.btitle.encode('utf8')


class HeroInfo(models.Model):
    hname = models.CharField(max_length=10)
    hgender = models.BooleanField(default=False)
    hcontent = models.CharField(max_length=1000)
    isDelete = models.BooleanField(default=False)
    book = models.ForeignKey(BookInfo)




