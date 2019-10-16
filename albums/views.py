# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import redirect, render, get_object_or_404, get_list_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse
from .models import Album, AlbumCategory, Photo, PhotoComment, AlbumTag
from django.db import connection
from django.core.paginator import Paginator
from datetime import datetime
import random

@login_required(login_url='signin')
def myalbums(request):
    #if request.user.is_authenticated:
    with connection.cursor() as cursor:
        cursor.execute("select DISTINCT a.id, a.name, a.total_views, c.`name` category , MIN(b.image) image, " +
            "count(a.id) totalphoto, a.adddate adddate from albums_album a, albums_photo b, albums_albumcategory c " +
            "where a.id = b.aid_id and a.category_id = c.id and a.uid_id = "+str(request.user.id)+" group by a.id")
        row = cursor.fetchall()

    albums = row
    paginator = Paginator(albums, 20)
    page = request.GET.get('page')
    albums = paginator.get_page(page)
    title = "MyAlbums"
    albums_cat = AlbumCategory.objects.all()
    context = {'albums' : albums, 'time': datetime.now(), 'title' : title, 'albums_cat' :  albums_cat}
    return render(request, 'myalbums.html', context)
    #else:
    #    return redirect('/signin/?next=/create-story/')

#@login_required(login_url='signin')
def album_photo(request, aid):

    photos = get_list_or_404(Photo, aid=aid)
    album = get_object_or_404(Album, pk=aid)
    title = album.name
    albums_cat = AlbumCategory.objects.all()
    

    album_item = Album.objects.all()
    len_album = len(album_item)
    if len_album > 4 :
        random_album =  random.sample(list(album_item), 5)
    else :
        random_album =  random.sample(list(album_item), len_album)

    context = {'photos': photos, 'album' : album, 'albums_cat' : albums_cat, 'random_album' : random_album, 'title' : title}
    
    if request.method == 'POST':
        user_id = request.user
        comment_post = request.POST['comment']
        comment = PhotoComment(pid=album, uid=user_id, comment=comment_post)
        comment.save()
        return redirect(reverse('album-photo', args=[aid]))
    return render(request, 'album-photo.html', context)

def albums(request, searchfor=None, search=None):
    if searchfor == 'album':
        with connection.cursor() as cursor:
            cursor.execute("select DISTINCT a.id, a.`name`, a.total_views, c.`name` category , MIN(b.image), " +
            "count(a.id) totalphoto from albums_album a, albums_photo b, albums_albumcategory c " +
            "where a.id = b.aid_id and a.category_id = c.id and (LOWER(c.name) REGEXP '" + search.lower() +"' " +
            "or LOWER(a.`name`) REGEXP '"+search.lower()+"' or LOWER(a.tags) REGEXP '"+search.lower()+"')  group by a.id")
            row = cursor.fetchall()
    else:
        with connection.cursor() as cursor:
            cursor.execute("select DISTINCT a.id, a.`name`, a.total_views, c.`name` category , MIN(b.image), count(a.id) totalphoto from albums_album a, albums_photo b, albums_albumcategory c where a.id = b.aid_id and a.category_id = c.id group by a.id")
            row = cursor.fetchall()

    albums = row
    paginator = Paginator(albums, 20)
    page = request.GET.get('page')
    albums = paginator.get_page(page)
    context = {'albums' : albums, 'time': datetime.now()}
    return render(request, 'albums.html', context)

@login_required(login_url='signin')
def upload_picture(request):

    #if request.user.is_authenticated:
    if request.method == 'POST' and request.FILES['pic_1']:

        pic_file = request.FILES['pic_1']
        user_id = request.user
        name = request.POST['name']
        tags = request.POST['tags']
        category = request.POST['category']
        #cat = AlbumCategory.objects.get(id=category)
        cat = get_object_or_404(AlbumCategory, pk=category)
        
        create_album = Album(uid=user_id, name=name, tags=tags, category=cat)
        create_album.save()
        
        # jumlah pic
        sum_pic = request.POST['sum_pic']
        
        for i in range(int(sum_pic)):
            pic_num = i + 1
            pic_file = 'pic_' + str(pic_num)
            pic_cap = 'pic_cap_' + str(pic_num)

            if request.FILES.get(pic_file, False) :
                pic_file = request.FILES[pic_file]
                pic_cap = request.POST[pic_cap]
                create_pic = Photo(aid=create_album, caption=pic_cap, image=pic_file)
                create_pic.save()

        # Proses Tagging
        list_tags = tags.split(',')
        list_tags = [i.strip().lower() for i in list_tags]
        
        for tg in list_tags:
            if AlbumTag.objects.filter(tag=tg).exists():
                current_tag = AlbumTag.objects.filter(tag=tg).first()
                current_tag.albums.add(create_album)
            else:
                create_tag = AlbumTag(uid=user_id, tag=tg)
                create_tag.save()
                create_tag.albums.add(create_album)
        
        ac_list = AlbumCategory.objects.all()
        context = {'ac_list' : ac_list}

        return render(request, 'upload-picture.html', context)
    else:

        ac_list = AlbumCategory.objects.all()
        context = {'ac_list' : ac_list}

        return render(request, 'upload-picture.html', context)
    #else:
    #    return redirect('/signin/?next=/upload/')

def album_category(request, slug):
    albums = get_list_or_404(Album.objects.order_by('-adddate'), category__slug=slug)
    category = AlbumCategory.objects.get(slug=slug)

    archive_title = 'Album Category : ' + category.name 
    albums_cat = AlbumCategory.objects.all()

    context = {'albums' : albums, 'archive_title':archive_title, 'albums_cat' :  albums_cat}
    return render(request, 'album-archive.html', context)

def album_tag(request, pk):
    albums = get_list_or_404(Album.objects.order_by('-adddate'), albumtag__id=pk)
    tag = AlbumTag.objects.get(pk=pk)

    archive_title = 'Album Tag : ' + tag.tag 
    albums_cat = AlbumCategory.objects.all()

    context = {'albums' : albums, 'archive_title':archive_title, 'albums_cat' :  albums_cat}
    return render(request, 'album-archive.html', context)