# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Video, VideoCategory
from django.contrib.auth.models import User
from django.http import HttpResponse
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

def video_category(request, slug):
    vids = get_list_or_404(Video.objects.order_by('-adddate'), category__slug=slug)
    category = VideoCategory.objects.get(slug=slug)

    archive_title = 'Video Category : ' + category.name 
    context = {'vids' : vids, 'archive_title':archive_title}
    return render(request, 'video-archive.html', context)

def video_channel(request, pk):
    vids = get_list_or_404(Video.objects.order_by('-adddate'), uid=pk)
    
    user = User.objects.get(pk=pk)
    archive_title = 'Video Channel : ' +  user.username
    context = {'vids' : vids, 'archive_title':archive_title}
    return render(request, 'video-archive.html', context)