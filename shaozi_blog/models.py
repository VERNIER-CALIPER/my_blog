from django.db import models
import os
from django.conf import settings

def get_article_content_path(instance,filename):
<<<<<<< HEAD
    return 'article/{0}/{1}'.format(
            instance.title,filename)
def get_article_image_comtent_path(instance,filename):
    return 'article/{0}/{1}'.format(
            instance.articles.title,filename)
=======

    if instance.article_id is not None :
        return 'article/{0}/{1}'.format(
                str(instance.article_id),filename)

    return 'article/{0}/{1}'.format(
            instance.tmp_dir,filename)

def get_article_image_comtent_path(instance,filename):

    if instance.articles.article_id is not None :
        return 'article/{0}/{1}'.format(
                str(instance.articles.article_id),filename)
>>>>>>> af1662806ecd6fcd697af8d8786b1030b37f3745

class Language(models.Model):
    color_choice=(
            ('NBLUE','normal_blue'),
            ('RED','red'),
            ('GRAY','gray'),
            ('GREEN','green'),
            ('SBLUE','sky_blue'),
            ('YELLOW','yellow'),
            )

    name=models.CharField(max_length=30,blank=False)
    color=models.CharField(max_length=8,
            choices=color_choice,
            default='NBLUE'
            )
    def __str__(self):
        return self.name

class Category(models.Model):
#The name should match the url (dict of views.model_cate_to_chinese)
    cate_to_html={'toy':'有趣','internet':'计算机网络',
            'data_aglo':'数据结构与算法','notes':'课程笔记',}
    cate_choice=(
            ('toy','toy'),
            ('internet','intetnet'),
            ('data_aglo','datastructure and alogrithms'),
            ('notes','some notes'),
            )

    category_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=40,choices=cate_choice,blank=False,null=False)
    article_num=models.IntegerField(default=0)
    language=models.ManyToManyField(Language)
    permission=models.CharField(max_length=20,null=False,blank=True,default='')

    def model_cate_to_chinese(self):
        return Category.cate_to_html[self.name]
    model_cate_to_chinese.short_description='分类名称'
    def __str__(self):
        return self.name

class Articles(models.Model):
    child_dir='article'
    #author,title and path can't be blank
    article_id=models.AutoField(primary_key=True)

    category=models.ManyToManyField(Category)
    language=models.ManyToManyField(Language)
    permission=models.CharField(max_length=10,null=False,blank=True,default='')

    author=models.ForeignKey('Author',on_delete=models.SET_NULL,
            blank=False,null=True)
    title=models.CharField(max_length=40,null=False,blank=False)
    submit_date=models.DateTimeField(auto_now_add=True)

    path=models.FileField(upload_to=get_article_content_path,blank=False)
    description=models.CharField(max_length=200,null=False,blank=True,default='nothing here')
#need rebuild
    @property
    def tmp_dir(self):
        if hasattr(self,'_tmp_dir'):
            return self._tmp_dir
        else:
            self._tmp_dir=self._create_tmpn_dir('article')
        return self._tmp_dir

    @tmp_dir.setter
    def tmp_dir(self,value):
        self._tmp_dir=value
        return self._tmp_dir

   #contentImage_set
    def __str__(self):
        return self.title

    def _create_tmpn_dir(self,child_dir):
        """1 child_dir should not start with '/' or end with '/'
           2 mkdir  MEDIA_ROOT/child_dir/tmpn                """

        if settings.MEDIA_ROOT[-1]=='/':
            cwd=settings.MEDIA_ROOT+child_dir+'/'
        else:
            cwd=settings.MEDIA_ROOT+'/'+child_dir+'/'

        num=0
        while True:
            dir_path=os.path.join(cwd,'tmp'+str(num))
            if not os.path.exists(dir_path):
                try:
                    os.makedirs(dir_path)
                except FileExistsError :
                    num+=1
                    continue
                return os.path.split(dir_path)[1]
            else :
                num+=1
                continue

    def time_for_html(self):
        return self.submit_date.strftime('%Y - %m - %d')
    class meta:
        ordering=['submit_date']

class Author(models.Model):
    #name of Author can't be blank.
    author_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=40,null=False,blank=False)
    description=models.CharField(max_length=100,null=False,blank=True)

    def __str__(self):
        return self.name
class ContentImage(models.Model):
    content_image=models.ImageField(upload_to=get_article_image_comtent_path)
    articles=models.ForeignKey(Articles)

    def __str__(self):
        return str(self.articles.article_id)
    __str__.short_description='related_article_id'
 #Create your models here.
