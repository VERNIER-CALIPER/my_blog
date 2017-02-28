from django.db import models

class Category(models.Model):
#The name should match the url (dict of views.model_cate_to_chinese)
    Category_id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=40,blank=False,null=False)
    article_num=models.IntegerField(default=0)
    generic_language=models.CharField(max_length=50,null=False,blank=True,default='')
    permission=models.CharField(max_length=20,null=False,blank=True,default='')


class Articles(models.Model):
    #author,title and path can't be blank
    article_id=models.IntegerField(primary_key=True)
    author=models.ForeignKey('Author',on_delete=models.SET('0'),
            blank=False,null=False)
    title=models.CharField(max_length=40,null=False,blank=False)
    submit_date=models.DateTimeField(auto_now_add=True)
    path=models.FileField(upload_to='article/%Y/%m/%d',blank=False)
    description=models.CharField(max_length=200,null=False,blank=True,default='nothing here')
    category=models.ManyToManyField(Category)
    language=models.CharField(max_length=50,null=False,blank=True,default='')
    permission=models.CharField(max_length=10,null=False,blank=True,default='')
#language firld should be like b:C;g:python;  b mean blue g mean gray
    class meta:
        ordering=['-submit-date']

class Author(models.Model):
    #name of Author can't be blank.
    author_id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=40,null=False,blank=False)
    description=models.CharField(max_length=100,null=False,blank=True)
# Create your models here.
