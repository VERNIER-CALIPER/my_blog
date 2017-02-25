from django.shortcuts import render
from shaozi_blog import models
from django.http import Http404
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
                    color_and_lang[1]=color_and_lang[1].center(6).replace(
                            ' ','&nbsp;')
                    an_article.lang.append(tuple(color_and_lang))
    return

def index(request):

    recent_articles=models.Articles.objects.all()[0:5]
    if recent_articles.count()!=0:
        model_lebal_to_bootstrap_style(recent_articles)
        return render(request,template_name='shaozi_blog/index.html',
                context={'article_set':recent_articles,})
    return render(request,template_name='shaozi_blog/index.html')


def category(request,cate):
    cate_articles=models.Articles.objects.filter(category__contains=cate)[0:5]
    model_lebal_to_bootstrap_style(cate_articles)
    return render(request,
        template_name='shaozi_blog/category.html',
        context={'article_set':cate_articles,})

def article(request,pk):
#the an_article_set is stupid to fit the model_lebal_to_bootstrap_style func
#and needed to rebuilded
    try:
        an_article_set=models.Articles.objects.filter(article_id=pk)
        model_lebal_to_bootstrap_style(an_article_set)
        content=an_article_set[0].path.readlines()
        an_article_set[0].path.close()
    except (IndexError,FileNotFoundError,AttributeError) :
        raise Http404
    return render(request,
        template_name='shaozi_blog/article.html',
        context={'an_article':an_article_set[0],'content':content})
# Create your views here.
