from django.db.models import F
import os
from django.conf import settings
#need rebuild
def create_tmpn_dir(child_dir):
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


def add_dir_path_to_article(sender,**kwargs):
    if not kwargs['update_fields']:
        kwargs['instance'].tmp_dir=create_tmpn_dir('article')
    return


def replace_tmpn_to_article_id(sender,**kwargs):
#next two if need rebuild repalce 'article' with a commom var
    if settings.MEDIA_ROOT[-1]=='/':
        cwd=settings.MEDIA_ROOT+'article'+'/'
    else:
        cwd=settings.MEDIA_ROOT+'/'+'article'+'/'
    old_tmp=os.path.join(cwd,kwargs['instance'].tmp_dir)
    os.rename(
            old_tmp,
            os.path.join(os.path.split(old_tmp)[0],str(kwargs['instance'].article_id))
            )
    return



def article_add_change(sender,**kwargs):
    if kwargs['action']=='post_add':
        kwargs['instance'].category.all().update(
                article_num=F('article_num')+1)
    elif kwargs['action']=='pre_remove':
        kwargs['instance'].category.filter(
                category_id__in=kwargs['pk_set']
                ).update(article_num=F('article_num')-1)
    return


def article_delete(sender,**kwargs):
    kwargs['instance'].category.all().update(
            article_num=F('article_num')-1)
    return


