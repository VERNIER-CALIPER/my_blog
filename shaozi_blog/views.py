from django.shortcuts import render,get_object_or_404,redirect
from django.template import Template

from shaozi_blog import models
from django.http import Http404
from django.template import Context


"""
def model_lebal_to_bootstrap_style(articles):
#transmit color to bootstrap-style for template
#this dict to bootstrap is stupied. rebuild it in the future
    color_to_html={'b':'primary','a':'default','g':'success'
            ,'sb':'info','y':'warining','r':'danger'}
    for an_article in articles:
        an_article.lang=[]
        if an_article.language:
            for a_label in an_article.language.split(';'):
            #str.split will add an extra '' if
            #the split sign is not followed with word
                if a_label !='':
                    color_and_lang=a_label.split(':')
                    color_and_lang[0]=color_to_html[color_and_lang[0]]
                    an_article.lang.append(tuple(color_and_lang))
    return
"""



def model_lebal_to_bootstrap_style(articles):
#add .color_bootstrap attribute to an_article
    color_to_bootstrap={
            'NBLUE':'primary',
            'GRAY':'default',
            'SBLUE':'info',
            'YELLOW':'warning',
            'RED':'danger',
            'GREEN':'success'
            }
    for an_article in articles:
        an_article.lang=[]
        if an_article.language.all().exists():
            all_language=an_article.language.all()
            for a_language in all_language:
                an_article.lang+=[(color_to_bootstrap[a_language.color],a_language.name)]

    return

def index(request):
    recent_articles=models.Articles.objects.all()[0:5]
    if recent_articles.count()!=0:
        model_lebal_to_bootstrap_style(recent_articles)
        return render(request,template_name='shaozi_blog/index.html',
                context={'article_set':recent_articles,})
    return render(request,template_name='shaozi_blog/index.html')

def category(request,cate):

    category=get_object_or_404(models.Category,name=cate)
    article_set=category.articles_set.all()
    model_lebal_to_bootstrap_style(article_set)

    return render(request,
        template_name='shaozi_blog/category.html',
        context={'article_set':article_set,'cate':category.model_cate_to_chinese(),})

def article(request,pk):
#the an_article_set is stupid to fit the model_lebal_to_bootstrap_style func
#and needed  rebuilded
#rebuild for loop  in this block to a tag/fountion
    try:
        an_article_set=models.Articles.objects.filter(article_id=pk)

        model_lebal_to_bootstrap_style(an_article_set)

        an_article=an_article_set[0]
        content=an_article_set[0].path.readlines()
        an_article_set[0].path.close()
        flag=0
        for line in content:
            if line.lstrip().startswith(b'***'):
                line=line.replace(b'***',b'   ',1)
                content[flag]=Template(line).render(Context({'article_id':str(an_article.article_id)}),)
            flag+=1

    except IndexError :
        raise Http404
    return render(request,
        template_name='shaozi_blog/article.html',
        context={'an_article':an_article,'content':content})


def profile(request):
    return render(request,template_name='shaozi_blog/base.html')

#only for test
def errortest(request):
    return render(request,template_name='404.html')
# Create your views here.
