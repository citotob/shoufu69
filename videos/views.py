# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from .models import Video, VideoCategory
import random

def video_page(request, pk):
    video = get_object_or_404(Video, pk=pk)
    
    video_item = Video.objects.all()
    len_video = len(video_item)
    if len_video > 7 :
        random_video =  random.sample(list(video_item), 6)
    else :
        random_video =  random.sample(list(video_item), len_video)

    context = {'video': video , 'random_video' : random_video }
    return render(request, 'video-page.html', context)