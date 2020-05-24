#-*-coding:utf8-*-
# from haystack import indexes
# from .models import *
#
# class TestIndex(indexes.SearchIndex,indexes.Indexable):
#     text = indexes.CharField(document=True,use_template=True)
#     def get_model(self):
#         return HeroInfo
#     def index_queryset(self,using=None):
#         return self.get_model().objects.all()

from haystack import indexes
from .models import HeroInfo


class HeroInfoIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return HeroInfo

    def index_queryset(self, using=None):
        return self.get_model().objects.all()
