from django.apps import AppConfig
from django.db.models.signals import m2m_changed,pre_delete
from .receiver import article_add_change,article_delete


class ShaoziBlogConfig(AppConfig):
    name = 'shaozi_blog'
    def ready(self):
        from .models import Articles
        m2m_changed.connect(article_add_change,sender=Articles.category.through)
        pre_delete.connect(article_delete,sender=Articles)
