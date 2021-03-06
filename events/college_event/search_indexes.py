import datetime
from haystack.indexes import *
from models import Postevent
# from models import SubCategory
from django.contrib.auth.models import User
from haystack.management.commands import update_index
from django.template import RequestContext

class PosteventIndex(SearchIndex, Indexable):  
    text = CharField(document=True, use_template=True)
    searchtext = CharField()
    festtype = CharField(model_attr='festtype__id')
    # print 'festtype', festtype    
    city = CharField(model_attr='city__id')    
    festname = CharField(model_attr='festname')
    # category = CharField(model_attr='category__id')
    # subcategoryid = CharField(model_attr='subcategory__id')         
    


    def autoUpdateRebuild_index(self):
        update_index.Command().handle()
        rebuild_index.Command().handle()

    # def prepare_searchtext(self, obj):
    #     text = []
    #     if obj.festname:
    #         text.append(obj.festname)
    #         print"text title", text
    #     if obj.festtype:
    #         text.append(obj.festtype)
    #         print"text description", text 
    #     #text += self.prepare_locations(obj)
    #     # text += obj.country
    #     print "text", text
    #     search = []
    #     for t in text:
    #         t = re.sub(r'[^\w]', ' ', t, flags=re.UNICODE).split(' ')
    #         for q in t:
    #             if q and (not re.match(r'[^\w]', q, flags=re.UNICODE)):
    #                 search.append(q)
    #     return ' '.join(search)

    # def prepare_locations(self,obj):
    #     countrys=[]
    #     country=obj.country
    #     countrycode=Country.objects.get(code=country)
    #     print "country", country
    #     print "countrycode", countrycode.code
    #     countrys.append(countrycode.code)
    #     return countrys
    
    def get_model(self):
        return Postevent
    
    def index_queryset(self, **kwargs):
        print 'index_queryset'       
        postevent = Postevent.objects.all()       
        return postevent

# class SubCategoryIndex(SearchIndex, Indexable):
#     text = CharField(document=True, use_template=True)
#     searchtext = CharField()
#     # category = CharField(model_attr='category__id')
#     subcategory = CharField(model_attr='name') 

#     def get_model(self):
#         return SubCategory

#     def index_queryset(self, **kwargs):
#         print 'index_queryset subcategory'
#         subcategories = SubCategory.objects.all()
#         return subcategories        

# register_model_for_search(Product, ProductIndex)
