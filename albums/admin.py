# encoding: utf-8
from django.contrib import admin
from jet.admin import CompactInline
from albums.models import Album, AlbumCategory
from django.utils.translation import ugettext_lazy as _

class AlbumAdmin(admin.ModelAdmin):
      list_display    = ['uid', 'name', 'tags', 'category', 'total_photos', 'total_views',
                        'type', 'addtime', 'status', 'adddate', 'rate', 'ratedby',
                        'total_comments', 'total_favorites', 'likes', 'dislikes']

#class AlbumCategoryAdmin(admin.ModelAdmin):
#      list_display    = ['name', 'slug', 'total_albums']

class AlbumCategoryAdmin(admin.ModelAdmin):
      list_display    = ['uid', 'name', 'slug', 'thumb']

admin.site.register(Album, AlbumAdmin)
admin.site.register(AlbumCategory, AlbumCategoryAdmin)