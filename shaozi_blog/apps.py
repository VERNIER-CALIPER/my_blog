from django.apps import AppConfig
from django.db.models.signals import m2m_changed,pre_delete,pre_save,post_save
from . import receiver


class ShaoziBlogConfig(AppConfig):
    name = 'shaozi_blog'
    def ready(self):
        from .models import Articles
        m2m_changed.connect(receiver.article_add_change,sender=Articles.category.through)
        pre_delete.connect(receiver.article_delete,sender=Articles)
        pre_save.connect(receiver.add_dir_path_to_article,sender=Articles)
        post_save.connect(receiver.replace_tmpn_to_article_id,sender=Articles)
