# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
import datetime
from ckeditor.fields import RichTextField

# Create your models here.
class NoticeCategory(models.Model):
    uid = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(_('Name'),max_length=150, default='')
    slug = models.CharField(_('Slug'), max_length=120, default='')
    thumb = models.ImageField(default = 'no-img.jpg')

    class Meta:
        verbose_name = 'NoticeCategory'
        verbose_name_plural = 'NoticeCategories'
        #unique_together = ('name', 'state', 'county')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return ''

class Notice(models.Model):
    uid = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    category = models.ForeignKey(NoticeCategory, on_delete=models.CASCADE)
    title = models.CharField(_('Title'), max_length=255, default='')
    #content = models.TextField(_('Content'),blank=True)
    content = RichTextField(_('Content'))
    total_views = models.BigIntegerField(_('Total Views'),default=0)
    total_comments = models.BigIntegerField(_('Total Comments'),default=0)
    total_links = models.BigIntegerField(_('Total Links'),default=0)
    addtime =  models.BigIntegerField(_('Add Time'),default=0)
    adddate = models.DateField(_('Add Date'),default=datetime.date.today)
    STATUS = (
        ('0','Suspended'),
        ('1','Active')
    )
    status = models.CharField(_('Status'),max_length=1, choices=STATUS,default='1')
    
    class Meta:
        verbose_name = 'Notice'
        verbose_name_plural = 'Notices'
        #unique_together = ('name', 'state', 'county')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return ''

class NoticeComment(models.Model):
    nid = models.ForeignKey(Notice, on_delete=models.CASCADE)
    uid = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    comment = models.TextField(_('comment'),blank=True)
    addtime = models.BigIntegerField(_('addtime'),default=0)
    STATUS_ = (
        ('0','0'),
        ('1','1')
    )
    status = models.CharField(_('status'),max_length=1, choices=STATUS_,default='1')

    class Meta:
        verbose_name = 'NoticeComment'
        verbose_name_plural = 'NoticeComments'
        #unique_together = ('name', 'state', 'county')

    def __str__(self):
        return self.comment

    def get_absolute_url(self):
        return ''

class NoticeImage(models.Model):
    uid = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    addtime = models.BigIntegerField(_('Add Time'),default=0)
    extension = models.CharField(_('Extension'), max_length=5, default='')
    thumb = models.ImageField(default = 'no-img.jpg')
    
    class Meta:
        verbose_name = 'NoticeImage'
        verbose_name_plural = 'NoticeImages'
        #unique_together = ('name', 'state', 'county')

    def __str__(self):
        return self.extension

    def get_absolute_url(self):
        return ''
