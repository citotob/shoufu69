# -*- coding: utf-8 -*-
#from __future__ import unicode_literals

#from django.apps import AppConfig


#class VideosConfig(AppConfig):
#    name = 'videos'

from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class StoriesConfig(AppConfig):
    name = 'stories'
    verbose_name = _('Stories')
