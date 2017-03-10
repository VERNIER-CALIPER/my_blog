from django.db.models import F
from django.conf import settings
import os
import shutil
#need rebuild




def replace_tmpn_to_article_id(sender,**kwargs):
#next two if need rebuild repalce 'article' with a commom var
    if kwargs['created']:
        if settings.MEDIA_ROOT[-1]=='/':
            cwd=settings.MEDIA_ROOT+'article'+'/'
        else:
            cwd=settings.MEDIA_ROOT+'/'+'article'+'/'

        article_id_dir=os.path.join(cwd,str(kwargs['instance'].article_id))
        old_tmp=os.path.join(cwd,kwargs['instance'].tmp_dir)

        os.rename(
                old_tmp,
                article_id_dir,
                )

        init_name=kwargs['instance'].path.name
        kwargs['instance'].path.name=os.path.join(
                os.path.dirname(os.path.dirname(init_name)),
                os.path.join(str(kwargs['instance'].article_id),os.path.basename(init_name))
                )
        for img in kwargs['instance'].contentimage_set.all():
            init_name=img.name
            img.name=os.path.join(
                os.path.dirname(os.path.dirname(init_name)),
                os.path.join(str(kwargs['instance'].article_id),os.path.basename(init_name))
                )
        kwargs['instance'].save()

        return article_id_dir

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


