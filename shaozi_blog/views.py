from django.shortcuts import render

def index(request):
   return render(request,template_name='shaozi_blog/index.html')
def category(request,cate):
   return render(request,template_name='shaozi_blog/category.html')
def article(request,year,month,day,pk):
   return render(request,template_name='shaozi_blog/article.html')
# Create your views here.
