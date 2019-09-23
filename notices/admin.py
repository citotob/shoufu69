# encoding: utf-8
from django.contrib import admin
from jet.admin import CompactInline
from notices.models import Notice, NoticeCategory, NoticeComment, NoticeImage
from django.utils.translation import ugettext_lazy as _

class NoticeAdmin(admin.ModelAdmin):
    list_display    = ['uid', 'category', 'title', 'content', 'status']
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'uid':
            kwargs['initial'] = request.user.id
        return super(NoticeAdmin, self).formfield_for_foreignkey(
            db_field, request, **kwargs
        )
    #def save_model(self, request, obj, form, change):
    #  obj.uid = request.user
    #  obj.save()
    #def save_model(self, request, obj, form, change):
    #    obj.uid = request.user
    #    super().save_model(request, obj, form, change)
    #def save_model(self, request, obj, form, change):
    #    if not obj.pk:
    #        # Only set added_by during the first save.
    #        obj.uid = request.user
    #    super().save_model(request, obj, form, change)

class NoticeCategoryAdmin(admin.ModelAdmin):
    list_display    = ['uid', 'name', 'slug', 'thumb']

class NoticeImageAdmin(admin.ModelAdmin):
    list_display    = ['uid', 'thumb', 'addtime', 'extension']
    #readonly_fields = ('addtime', 'extension')
    fields    = ['uid', 'thumb']

admin.site.register(Notice, NoticeAdmin)
admin.site.register(NoticeCategory, NoticeCategoryAdmin)
admin.site.register(NoticeImage, NoticeImageAdmin)