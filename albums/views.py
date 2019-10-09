# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import redirect, render,  get_object_or_404, get_list_or_404

from django.http import HttpResponse
from .models import Album, AlbumCategory, Photo
from django.db import connection

import random

def albums(request):
    #albums = Album.objects.all().order_by('-adddate')
    #albums = Album.objects.all().prefetch_related('id')
    with connection.cursor() as cursor:
        cursor.execute("select DISTINCT a.id, a.`name`, a.total_views, c.`name` category , MIN(b.image), count(a.id) totalphoto, a.adddate, c.`slug` category from albums_album a, albums_photo b, albums_albumcategory c where a.id = b.aid_id and a.category_id = c.id group by a.id")
        row = cursor.fetchall()

    albums = row
    albums_cat = AlbumCategory.objects.all()
    context = {'albums' : albums, 'albums_cat' :  albums_cat}
    return render(request, 'albums.html', context)

def album_photo(request, aid):

    photos = get_list_or_404(Photo, aid=aid)
    album = get_object_or_404(Album, pk=aid)
    albums_cat = AlbumCategory.objects.all()
    

    album_item = Album.objects.all()
    len_album = len(album_item)
    if len_album > 4 :
        random_album =  random.sample(list(album_item), 5)
    else :
        random_album =  random.sample(list(album_item), len_album)

    context = {'photos': photos, 'album' : album, 'albums_cat' : albums_cat, 'random_album' : random_album}
    return render(request, 'album-photo.html', context)

def album_category(request, slug):
    albums = get_list_or_404(Album.objects.order_by('-adddate'), category__slug=slug)
    category = AlbumCategory.objects.get(slug=slug)

    archive_title = 'Album Category : ' + category.name 
    albums_cat = AlbumCategory.objects.all()

    context = {'albums' : albums, 'archive_title':archive_title, 'albums_cat' :  albums_cat}
    return render(request, 'album-archive.html', context)

def upload_picture(request):

    if request.user.is_authenticated:
        if request.method == 'POST' and request.FILES['pic_1']:

            pic_file = request.FILES['pic_1']
            user_id = request.user
            name = request.POST['name']
            tags = request.POST['tags']
            category = request.POST['category']
            cat = AlbumCategory.objects.get(id=category)
            
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

            
            ac_list = AlbumCategory.objects.all()
            context = {'ac_list' : ac_list}

            return render(request, 'upload-picture.html', context)
        else:

            ac_list = AlbumCategory.objects.all()
            context = {'ac_list' : ac_list}

            return render(request, 'upload-picture.html', context)
    else:
        return redirect('/signin/?next=/upload/')