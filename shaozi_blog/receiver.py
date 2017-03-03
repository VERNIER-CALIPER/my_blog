from django.db.models import F
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
