# -*- coding: utf-8 -*-
#from __future__ import unicode_literals

#from django.contrib import admin

# Register your models here.
#

# encoding: utf-8
from django.contrib import admin
from jet.admin import CompactInline
from videos.models import Video, VideoComment
from django.utils.translation import ugettext_lazy as _


#class VideoInline(admin.TabularInline):
#    model = Video
#    extra = 1
#    show_change_link = True


#class VideoCitiesInline(CompactInline):
#    model = Video
#    extra = 1
#    show_change_link = True


#class VideoAdmin(admin.ModelAdmin):
#    inlines = (StateCountiesInline, StateCitiesInline)

class VideoAdmin(admin.ModelAdmin):
      list_display    = ['uid', 'title', 'description', 'featuredesc', 'keyword', 'channel',
                        'vdoname', 'flvdoname', 'formats', 'lformats', 'duration', 'space',
                        'type', 'addtime', 'adddate', 'recorddate', 'location', 'country',
                        'vkey', 'viewnumber', 'viewtime', 'com_num', 'fav_num', 'download_num',
                        'featured', 'ratedby', 'rate', 'filehome', 'be_comment', 'be_rated',
                        'embed', 'embed_code', 'thumb', 'thumbs', 'voter_id','server', 'active',
                        'hd_filename', 'ipod_filename', 'aspect_hd', 'width_hd', 'height_hd',
                        'aspect_sd', 'width_sd', 'height_sd', 'iphone', 'hd', 'likes', 'dislikes']

class VideoCommentAdmin(admin.ModelAdmin):
      list_display    = ['vid', 'uid', 'comment', 'addtime', 'status']

admin.site.register(Video, VideoAdmin)
admin.site.register(VideoComment, VideoCommentAdmin)