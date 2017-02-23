from django.db import models

class Articles(models.Model):
    article_id=models.IntegerField(primary_key=True)
    author=models.ForeignKey('Author',on_delete=models.SET('0'),
            blank=False,null=False)
    title=models.CharField(max_length=40)
    submit_date=models.DateTimeField(auto_now_add=True)
    path=models.FileField(upload_to='article/%Y/%m/%d')
    description=models.CharField(max_length=200,null=True)
    category=models.CharField(max_length=40,null=True)
    permission=models.CharField(max_length=10,null=True)

    class meta:
        ordering=['-submit-date']

class Author(models.Model):
    author_id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=40)
    description=models.CharField(max_length=100)
# Create your models here.
