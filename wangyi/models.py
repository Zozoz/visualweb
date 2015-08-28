import datetime

from django.db import models
from django.utils import timezone


class WangyiArticle(models.Model):
    docid = models.CharField(primary_key=True, max_length=50)
    url = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    digest = models.CharField(max_length=200)
    source = models.CharField(max_length=50)
    ptime = models.DateTimeField()
    mtime = models.DateTimeField()
    comments_url = models.CharField(max_length=200)
    comments_number = models.IntegerField(default=0)
    votecount = models.IntegerField(default=0)
    replycount = models.IntegerField(default=0)
    content = models.TextField()
    parent_id = models.CharField(max_length=50)
    url_3w = models.CharField(max_length=200)

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

"""
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published', default='1900-00-00 00:00:00')
    description = models.CharField(max_length=1000, default='')

    def __unicode__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    vote_date = models.DateTimeField('date vote', default='1900-00-00 00:00:00')


    def __unicode__(self):
        return self.choice_text

"""
