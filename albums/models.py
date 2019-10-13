# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
import datetime

# Create your models here.
class AlbumCategory(models.Model):
    uid = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(_('Name'),max_length=150, default='')
    slug = models.CharField(_('Slug'), max_length=120, default='')
    thumb = models.ImageField(default = 'no-img.jpg')

    class Meta:
        verbose_name = 'AlbumCategory'
        verbose_name_plural = 'AlbumCategories'
        #unique_together = ('name', 'state', 'county')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return ''

class Album(models.Model):
    uid = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(_('Name'), max_length=255, default='')
    tags =  models.TextField(_('Tags'), blank=True)
    category = models.ForeignKey(AlbumCategory, on_delete=models.CASCADE)
    total_photos = models.BigIntegerField(_('Total photos'),default=0)
    total_views = models.BigIntegerField(_('Total Views'),default=0)
    TYPE = (
        ('1','Public'),
        ('0','Private')
    )
    type = models.CharField(_('Type'),max_length=1, choices=TYPE,default='1')
    addtime = models.BigIntegerField(_('Addtime'),default=0)
    STATUS = (
        ('0','Suspended'),
        ('1','Active')
    )
    status = models.CharField(_('Status'),max_length=1, choices=STATUS,default='1')
    #adddate = models.DateField(_('Adddate'),default=timezone.now)
    adddate = models.DateTimeField(_('Add Date'),auto_now_add=True)
    rate = models.FloatField(_('Rate'),default=0)
    ratedby = models.BigIntegerField(_('Ratedby'),default=0)
    total_comments = models.BigIntegerField(_('Total Comments'),default=0)
    total_favorites = models.BigIntegerField(_('Total Favorites'),default=0)
    likes = models.BigIntegerField(_('Likes'),default=0)
    dislikes = models.BigIntegerField(_('Dislikes'),default=0)

    class Meta:
        verbose_name = 'Album'
        verbose_name_plural = 'Albums'
        #unique_together = ('name', 'state', 'county')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return ''

class Photo(models.Model):
    aid = models.ForeignKey(Album, on_delete=models.CASCADE)
    image = models.ImageField(upload_to = 'photo/%Y/%m/%d', default = 'no-img.jpg')
    caption = models.CharField(_('Caption'),max_length=100, default='')
    total_views = models.BigIntegerField(_('Total Views'),default=0)
    total_comments = models.BigIntegerField(_('Total Comments'),default=0)
    STATUS = (
        ('0','Suspended'),
        ('1','Active')
    )
    status = models.CharField(_('Status'),max_length=1, choices=STATUS,default='1')
    rate = models.FloatField(_('Rate'),default=0)
    ratedby = models.BigIntegerField(_('Ratedby'),default=0)
    total_favorites = models.BigIntegerField(_('Total Favorites'),default=0)
    TYPE = (
        ('1','Public'),
        ('0','Private')
    )
    type = models.CharField(_('Type'),max_length=1, choices=TYPE,default='1')
    likes = models.BigIntegerField(_('Likes'),default=0)
    dislikes = models.BigIntegerField(_('Dislikes'),default=0)

    class Meta:
        verbose_name = 'Photo'
        verbose_name_plural = 'Photos'
        #unique_together = ('name', 'state', 'county')

    def __str__(self):
        return self.caption

    def get_absolute_url(self):
        return ''

class PhotoComment(models.Model):
    pid = models.ForeignKey(Album, on_delete=models.CASCADE)
    uid = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    comment = models.TextField(_('Comment'),blank=True)
    addtime = models.DateTimeField(_('Add Time'),auto_now_add=True)
    STATUS_ = (
        ('0','Suspended'),
        ('1','Active')
    )
    status = models.CharField(_('Status'),max_length=1, choices=STATUS_,default='1')

    class Meta:
        verbose_name = 'PhotoComment'
        verbose_name_plural = 'PhotoComments'
        #unique_together = ('name', 'state', 'county')

    def __str__(self):
        return self.comment

    def get_absolute_url(self):
        return ''

class PhotoFavorite(models.Model):
    pid = models.ForeignKey(Photo, on_delete=models.CASCADE)
    uid = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'PhotoFavorite'
        verbose_name_plural = 'PhotoFavorite'
        #unique_together = ('name', 'state', 'county')

    def __str__(self):
        return self.pid

    def get_absolute_url(self):
        return ''

class PhotoFlag(models.Model):
    pid = models.ForeignKey(Photo, on_delete=models.CASCADE)
    uid = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    reason = models.CharField(_('Reason'),max_length=15, default='')
    message = models.TextField(_('Message'),blank=True)
    add_date = models.DateField(_('Add Date'),default=datetime.date.today)

    class Meta:
        verbose_name = 'PhotoFlag'
        verbose_name_plural = 'PhotoFlags'
        #unique_together = ('name', 'state', 'county')

    def __str__(self):
        return self.reason

    def get_absolute_url(self):
        return ''

class PhotoRatingId(models.Model):
    pid = models.ForeignKey(Photo, on_delete=models.CASCADE)
    uid = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'PhotoRatingId'
        verbose_name_plural = 'PhotoRatingId'
        #unique_together = ('name', 'state', 'county')

    def __str__(self):
        return self.pid

    def get_absolute_url(self):
        return ''

class PhotoRatingIp(models.Model):
    pid = models.ForeignKey(Photo, on_delete=models.CASCADE)
    ip = models.IntegerField(_('IP'),default=0)

    class Meta:
        verbose_name = 'PhotoRatingIp'
        verbose_name_plural = 'PhotoRatingIp'
        #unique_together = ('name', 'state', 'county')

    def __str__(self):
        return self.ip

    def get_absolute_url(self):
        return ''


class AlbumTag(models.Model):
    tag = models.CharField(max_length=20)
    uid = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    albums = models.ManyToManyField(Album)
    
    def __str__(self):
        return self.tag