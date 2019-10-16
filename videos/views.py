# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.core.paginator import Paginator
from datetime import datetime
from django.shortcuts import redirect, render, get_object_or_404, get_list_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.db.models import F
from django.core import serializers
from django.conf import settings
import json
from django.core.cache import cache

from videos.models import Video, VideoCategory, VideoVoteUser
import random
from os.path import join as isfile
import os

from .forms import VideoForm

@login_required(login_url='signin')
def myvideos(request):
    #if request.user.is_authenticated:
    vids = Video.objects.filter(uid=request.user).order_by('-adddate')
    #title = str(request.user).capitalize() + "'s Video(s)"
    for vid in vids:
        title_b = vid.title1.decode()
        vid.title1 = title_b
    title = "MyVideos"
    paginator = Paginator(vids, 20)
    page = request.GET.get('page')
    vids = paginator.get_page(page)
    context = {'vids' : vids, 'time': datetime.now(), 'title' : title}
    return render(request, 'myvideos.html', context)
    #else:
    #    return redirect('/signin/?next=/create-story/')

#@login_required(login_url='signin')
def video_page(request, pk):
    video = get_object_or_404(Video, pk=pk)
    video.viewnumber = video.viewnumber + 1
    title = video.title
    video.save()

    video_item = Video.objects.all()
    len_video = len(video_item)
    if len_video > 7 :
        random_video =  random.sample(list(video_item), 6)
    else :
        random_video =  random.sample(list(video_item), len_video)

    #vid = Video.objects.get(video_id=video_id)

    blike = 0
    if request.user.is_authenticated:
        vid_like = VideoVoteUser.objects.filter(vid_id=int(pk), uid_id = request.user, status='1')
        
        if vid_like:
            blike = 1

    bdislike = 0
    if request.user.is_authenticated:
        vid_dislike = VideoVoteUser.objects.filter(vid_id=int(pk), uid_id = request.user, status='0')
        
        if vid_dislike:
            bdislike = 1

    if request.method == 'POST':
        user_id = request.user
        comment_post = request.POST['comment']
        comment = VideoComment(vid=video, uid=user_id, comment=comment_post)
        comment.save()
        return redirect(reverse('video-page', args=[pk]))

    context = {'video': video , 'random_video' : random_video, 'title' : title, 'blike' : blike, 'bdislike' : bdislike }
    return render(request, 'video-page.html', context)

#@login_required(login_url='signin')
def videolikes(request):
    vid_id = None
    if request.method == 'GET':
        vid_id = request.GET['video_id']
       
    likes = 0
    
    if vid_id:
        vid = Video.objects.get(id=int(vid_id))
        likes = vid.likes
        if request.user.is_authenticated:
            #likes = Video.objects.filter(pk=vid_id).update(likes=F('likes')+1)
            if vid:
                vid_like = VideoVoteUser.objects.filter(vid_id=int(vid_id), uid_id = request.user, status='1')
                
                if len(vid_like) == 0:
                    likes = vid.likes + 1
                    vid.likes =  likes
                    vid.save()

                    insert_vid_like = VideoVoteUser(vid_id=vid_id, uid=request.user, status = '1')
                    insert_vid_like.save()

    return HttpResponse(likes)

def videodislikes(request):
    vid_id = None
    if request.method == 'GET':
        vid_id = request.GET['video_id']
       
    dislikes = 0
    
    if vid_id:
        vid = Video.objects.get(id=int(vid_id))
        dislikes = vid.dislikes
        if request.user.is_authenticated:
            if vid:
                vid_dislike = VideoVoteUser.objects.filter(vid_id=int(vid_id), uid_id = request.user, status='0')
                
                if len(vid_dislike) == 0:
                    dislikes = vid.dislikes + 1
                    vid.dislikes =  dislikes
                    vid.save()

                    insert_vid_dislike = VideoVoteUser(vid_id=vid_id, uid=request.user, status = '0')
                    insert_vid_dislike.save()

    return HttpResponse(dislikes)

@login_required(login_url='signin')
def videodelete(request, video_id):
    vid = Video.objects.get(id=video_id)
    thumb = str(vid.thumb)
    videofile = str(vid.videofile)
    vid_name = thumb.split(".")
    
    videovoteuser = VideoVoteUser.objects.filter(vid=video_id, uid=request.user)
    videovoteuser.delete()
    
    for i in range(1,30):
        try:
            if os.path.isfile(vid_name[0][0:-1]+str(i)+"."+vid_name[1]):
                os.remove(vid_name[0][0:-1]+str(i)+"."+vid_name[1])
        except:
            break
    
    if os.path.isfile(settings.MEDIA_ROOT+"/"+videofile):
        os.remove(settings.MEDIA_ROOT+"/"+videofile)
    vid.delete()

    vids = Video.objects.filter(uid=request.user).order_by('-adddate')
    
    title = "MyVideos"
    paginator = Paginator(vids, 20)
    page = request.GET.get('page')
    vids = paginator.get_page(page)
    context = {'vids' : vids, 'time': datetime.now(), 'title' : title}
    return render(request, 'myvideos.html', context)

@login_required(login_url='signin')
def videoedit(request, video_id):
    instance = Video.objects.get(id=video_id)
    if request.method == 'POST':
        form = VideoForm(request.POST, instance=instance)
        if form.is_valid() :
            form.save()
            
            category_id = instance.category.id
            vc_list = VideoCategory.objects.all()
            context = {'form' : form, 'vc_list' : vc_list, 'category_id' : category_id}
            return render(request, 'edit-video.html', context)
    else :
        category_id = instance.category.id
        form = VideoForm(instance=instance)
    
    vc_list = VideoCategory.objects.all()
    context = {'form' : form, 'vc_list' : vc_list, 'category_id' : category_id}
    return render(request, 'edit-video.html', context)

def get_upload_progress(request):
    cache_key = "%s_%s" % (request.META['REMOTE_ADDR'], request.GET['X-Progress-ID'])
    data = cache.get(cache_key)
    return HttpResponse(json.dumps(data))

def video_category(request, slug):
    vids = get_list_or_404(Video.objects.order_by('-adddate'), category__slug=slug)
    category = VideoCategory.objects.get(slug=slug)

    archive_title = 'Video Category : ' + category.name 
    context = {'vids' : vids, 'archive_title':archive_title}
    return render(request, 'video-archive.html', context)

def video_tag(request, pk):
    vids = get_list_or_404(Video.objects.order_by('-adddate'), videotag__id=pk)
    tag = VideoTag.objects.get(pk=pk)

    archive_title = 'Video Tag : ' + tag.tag 
    context = {'vids' : vids, 'archive_title':archive_title}
    return render(request, 'video-archive.html', context)

def video_channel(request, pk):
    vids = get_list_or_404(Video.objects.order_by('-adddate'), uid=pk)
    
    user = User.objects.get(pk=pk)
    archive_title = 'Video Channel : ' +  user.username
    context = {'vids' : vids, 'archive_title':archive_title}
    return render(request, 'video-archive.html', context)
