import datetime
from django.db import models

from django.utils import timezone


class Article(models.Model):
    article_title = models.CharField('Name of article', max_length=30)
    article_text = models.TextField('Text of article')
    pub_date = models.DateTimeField('Pulish date')

    def __str__(self):
        return self.article_title

    def was_published_recently(self):
        return self.pub_date >= (timezone.now() - datetime.timedelta(days=7))

class Comment(models.Model):
   article = models.ForeignKey(Article, on_delete = models.CASCADE)
   author_name = models.CharField('Name of author', max_length=30)
   comment_text = models.CharField('Text of comment', max_length=30)

   def __str__(self):
        return self.author_name