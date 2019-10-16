# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings

from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, get_list_or_404, get_object_or_404, render
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.utils.translation import ugettext
from django.utils.encoding import smart_text, force_text, smart_bytes
from django.db import connection
from django.core.paginator import Paginator
from django.db.models import Q

import subprocess
from ffmpy import FFmpeg
import os
import re
from decimal import Decimal
from moviepy.video.io.VideoFileClip import VideoFileClip


from videos.forms import VideoForm
from videos.models import VideoCategory, Video, VideoThumbnails, VideoTag
from albums.views import albums
from stories.views import stories
import ast
from itertools import chain


#@login_required
def home(request, searchfor=None, search=None):
    if searchfor == 'video':
        vids = Video.objects.filter(Q(category__name__icontains=search) | 
                        Q(title__icontains=search) |
                        Q(description__icontains=search) |
                        Q(tags__icontains=search)).order_by('-adddate')
    else:
        vids = Video.objects.all().order_by('-adddate')

    for vid in vids:
        title_b = vid.title1.decode()
        vid.title1 = title_b
    
    paginator = Paginator(vids, 20)
    page = request.GET.get('page')
    vids = paginator.get_page(page)

    vids_popular = Video.objects.all().order_by('-viewnumber')[:8]

    context = {'vids' : vids, 'vids_popular' : vids_popular}
    return render(request, 'index.html', context)

def search(request):
    if request.method == 'POST':
        searchfor=request.POST['searchfor']
        search=request.POST['search']

        if searchfor=='video':
            return home(request, searchfor, search)
        elif searchfor=='album':
            return albums(request, searchfor, search)
        else:
            return stories(request, searchfor, search)
    else:
        searchfor=None
        search=None

        return home(request, searchfor, search)
    
    '''
    if request.method == 'POST':
        searchfor=request.POST['searchfor']
        search=request.POST['search']

        if searchfor=='Video':

            #vids = Video.objects.filter(Q(category__icontains=search) | 
            #            Q(title__icontains=search) |
            #            Q(description__icontains=search) |
            #            Q(tags__icontains=search)).order_by('-adddate')
        elif searchfor=='Album':
            with connection.cursor() as cursor:
        cursor.execute("select DISTINCT a.id, a.`name`, a.total_views, c.`name` category , MIN(b.image), count(a.id) totalphoto from albums_album a, albums_photo b, albums_albumcategory c where a.id = b.aid_id and a.category_id = c.id group by a.id")
        row = cursor.fetchall()

    albums = row
        else:
            vids = Video.objects.filter(Q(category__icontains=search) | 
                        Q(title__icontains=search) |
                        Q(description__icontains=search) |
                        Q(tags__icontains=search)).order_by('-adddate')

        vids = Video.objects.all().order_by('-adddate')
        paginator = Paginator(vids, 20)
        page = request.GET.get('page')
        vids = paginator.get_page(page)

        vids_popular = Video.objects.all().order_by('-viewnumber')[:8]

        context = {'vids' : vids, 'vids_popular' : vids_popular}
        return render(request, 'index.html', context)
    '''

def signin(request):
    return render(request, 'login.html')

@login_required(login_url='signin')
def upload(request):
    #if request.user.is_authenticated:
    return render(request, 'upload.html')
    #else:
        #return render(request, 'index.html')
    #    return redirect('/signin/?next=/upload/')
    #return render(request,'upload.html')

def get_video_length(path):
    clip = VideoFileClip(path)
    dur = int(clip.duration)
    hrs, mins, secs = dur//60//60, dur//60%60, dur%60
 
    hrs = "0"+str(hrs) if(hrs<10) else str(hrs)
    mins = "0"+str(mins) if(mins<10) else str(mins)
    secs = "0"+str(secs) if(secs<10) else str(secs)
 
    return dur


@login_required(login_url='signin')
def upload_video(request):
    #return render(request,'upload-video.html')
    #if request.user.is_authenticated:
    if request.method == 'POST' and request.FILES['video_file']:
        video_file = request.FILES['video_file']
        
        #fs = FileSystemStorage()
        #filename = fs.save(video_file.name, video_file)
        #uploaded_file_url = fs.url(filename)
        #vid_file = '%s/%s' % (settings.MEDIA_ROOT, video_file.name)
        
        #subprocess.call(['ffmpeg', '-i', vid_file, '-ss', '00:00:00.000', '-vframes', '1', img_output_path])
        
        #video_id = Video.objects.count()
        #video_id+=1
        #img_output_path = '%s/thumbnails/%s_%s' % (settings.MEDIA_ROOT, video_file.name, video_id)
        #img_output_path = '%s/thumbnails/%s' % (settings.MEDIA_ROOT, video_id)
        #img_output_path_url = '%sthumbnails/%s' % (settings.MEDIA_URL, video_id)
        #print(img_output_path_url)
        user_id = request.user
        
        
        title = request.POST['title']
        desc = request.POST['description']
        tags = request.POST['tags']
        category = request.POST['category']
        
        cat = VideoCategory.objects.get(id=category)
        #vid = Video(video_id=video_id, uid=user_id, title=title, description=desc, tags=tags, category=cat,videofile=video_file, thumb=img_output_path)
        #vid = Video(video_id=1, uid=user_id, title=title, description=desc, tags=tags, category=cat,videofile=video_file, thumb='img_output_path')
        
        try:
            vid = Video(video_id=1, uid=user_id, title=title, description=desc, tags=tags, category=cat,videofile='video_file', thumb='img_output_path')
            vid.save()
        except:
            
            title = request.POST['title'].encode('utf-8')
            title1 = request.POST['title'].encode('utf-8')
            desc = request.POST['description'].encode('utf-8')
            tags = request.POST['tags'].encode('utf-8')
            #category = request.POST['category'].encode('utf-8')

            vid = Video(video_id=1, uid=user_id, title=title, title1=title1, description=desc, tags=tags, category=cat,videofile='video_file', thumb='img_output_path')
            vid.save()
        video_id = vid.id
        
        vid = Video.objects.get(id=video_id)
        img_output_path = '%s/thumbnails/%s' % (settings.MEDIA_ROOT, video_id)
        img_output_path_url = '%sthumbnails/%s' % (settings.MEDIA_URL, video_id)
        vid.video_id = video_id
        vid.videofile = video_file
        vid.save()
        
        #vid = Video.objects.get(id=video_id)
        #vid_id = Video.objects.get(id=vid.id)
        #ff = FFmpeg(inputs={vid.videofile.path: None}, outputs={img_output_path+'_%d.jpg': ['-vframes', '20']})
        #ff = FFmpeg(inputs={vid.videofile.path: None}, outputs={img_output_path+'_%d.jpg': ['-vf', 'fps=1/60', '-vframes', '20']})
        duration = get_video_length(vid.videofile.path)
        pertime = duration/20
        #print(pertime)
        ff = FFmpeg(inputs={vid.videofile.path: None}, outputs={img_output_path+'_%d.jpg': ['-vf', 'fps=1/'+str(pertime), '-vframes', '20']})
        #print(ff.cmd)
        ff.run()
        
        #duration = get_video_length(vid.videofile.path)
        #print(duration)
        #video_path_url = '%s/%s' % (settings.MEDIA_ROOT, vid.videofile.path)
        #print(vid.videofile.path)
        #duration = getLength(vid.videofile.path)
        #print(duration)

        vid.thumb = img_output_path + '_1.jpg'
        vid.thumb_url = img_output_path_url + '_1.jpg'
        vid.duration = duration
        vid.save()

        # Proses Tagging
        list_tags = tags.split(',')
        list_tags = [i.strip().lower() for i in list_tags]
        
        for tg in list_tags:
            if VideoTag.objects.filter(tag=tg).exists():
                current_tag = VideoTag.objects.filter(tag=tg).first()
                current_tag.videos.add(vid)
            else:
                create_tag = VideoTag(uid=user_id, tag=tg)
                create_tag.save()
                create_tag.videos.add(vid)

        vc_list = VideoCategory.objects.all()
        context = {'vc_list' : vc_list}

        return render(request, 'upload-video.html', context)
    else:
        vc_list = VideoCategory.objects.all()
        form = VideoForm()
        context = {'form' : form, 'vc_list' : vc_list}
        return render(request, 'upload-video.html', context)
    #else:
    #    return redirect('/signin/?next=/upload/')

@login_required(login_url='signin')
def upload_picture(request):
    #return render(request,'upload-picture.html')
    #if request.user.is_authenticated:
    return render(request, 'upload-picture.html')
    #else:
    #    return redirect('/signin/?next=/upload/')
    
