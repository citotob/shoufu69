# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
import datetime

# Create your models here.
@python_2_unicode_compatible
class StoryCategory(models.Model):
    uid = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(_('Name'),max_length=150, default='')
    slug = models.CharField(_('Slug'), max_length=120, default='')
    thumb = models.ImageField(default = 'no-img.jpg')

    class Meta:
        verbose_name = 'StoryCategory'
        verbose_name_plural = 'StoryCategories'
        #unique_together = ('name', 'state', 'county')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return ''

@python_2_unicode_compatible
class Story(models.Model):
    uid = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    category = models.ForeignKey(StoryCategory, on_delete=models.CASCADE)
    title = models.CharField(_('Title'), max_length=255, default='')
    content = models.TextField(_('Content'),blank=True)
    total_views = models.BigIntegerField(_('Total Views'),default=0)
    total_comments = models.BigIntegerField(_('Total Comments'),default=0)
    total_links = models.BigIntegerField(_('Total Links'),default=0)
    addtime = models.BigIntegerField(_('Add time'),default=0)
    adddate = models.DateField(_('Add date'),default=datetime.date.today)
    STATUS_ = (
        ('0','0'),
        ('1','1')
    )
    status = models.CharField(_('Status'),max_length=1, choices=STATUS_,default='1')

    class Meta:
        verbose_name = 'Story'
        verbose_name_plural = 'Stories'
        #unique_together = ('name', 'state', 'county')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return ''

class StoryComment(models.Model):
    sid = models.ForeignKey(Story, on_delete=models.CASCADE)
    uid = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    comment = models.TextField(_('Comment'),blank=True)
    addtime = models.BigIntegerField(_('Addtime'),default=0)
    STATUS_ = (
        ('0','0'),
        ('1','1')
    )
    status = models.CharField(_('Status'),max_length=1, choices=STATUS_,default='1')

    class Meta:
        verbose_name = 'StoryComment'
        verbose_name_plural = 'StoryComments'
        #unique_together = ('name', 'state', 'county')

    def __str__(self):
        return self.comment

    def get_absolute_url(self):
        return ''

