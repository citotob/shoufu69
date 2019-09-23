# encoding: utf-8
from django.contrib import admin
from jet.admin import CompactInline
from stories.models import Story, StoryComment, StoryCategory
from django.utils.translation import ugettext_lazy as _

class StoryAdmin(admin.ModelAdmin):
      list_display    = ['uid', 'title', 'content', 'total_views', 'total_comments', 'total_links',
                        'addtime', 'adddate', 'status', ]

class StoryCommentAdmin(admin.ModelAdmin):
      list_display    = ['sid', 'uid', 'comment', 'addtime', 'status']

class StoryCategoryAdmin(admin.ModelAdmin):
      list_display    = ['uid', 'name', 'slug', 'thumb']

admin.site.register(Story, StoryAdmin)
admin.site.register(StoryComment, StoryCommentAdmin)
admin.site.register(StoryCategory, StoryCategoryAdmin)