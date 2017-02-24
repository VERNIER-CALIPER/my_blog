from django.shortcuts import render
from shaozi_blog import models
def index(request):
    recent_articles=models.Articles.objects.all()[0:5]
    if recent_articles.count()!=0:
        model_language_to_bootstrap_style(recent_articles)
        return render(request,template_name='shaozi_blog/index.html',
                context={'article_set':recent_articles,})
    return render(request,template_name='shaozi_blog/index.html')


def model_language_to_bootstrap_style(articles):
#transmit color to bootstrap-style for template 
#the color_to_html is not completed 
    color_to_html={'b':'primary',}
    for an_article in articles:
        an_article.lang=[]
        if an_article.language:
            for a_label in an_article.language.split(';'):
            #str.split will add an extra '' if
            #the split sign is not followed with word
                if a_label !='':
                    color_and_lang=a_label.split(':')
                    color_and_lang[0]=color_to_html[color_and_lang[0]]
                    color_and_lang[1]=color_and_lang[1].center(6).replace(' ',
                            '&nbsp;')
                    an_article.lang.append(tuple(color_and_lang))
    return

def category(request,cate):
   return render(request,template_name='shaozi_blog/category.html')
def article(request,pk):
   return render(request,template_name='shaozi_blog/article.html')
# Create your views here.
