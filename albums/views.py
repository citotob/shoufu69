# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the videos index.")


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