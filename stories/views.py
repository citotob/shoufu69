# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.urls import reverse

from stories.forms import StoryForm
from .models import StoryCategory, Story, StoryComment
from datetime import datetime

import random

def stories(request, searchfor=None, search=None):
    if searchfor == 'story':
        stories = Story.objects.filter(Q(category__name__icontains=search) | 
                        Q(title__icontains=search) |
                        Q(content__icontains=search)).order_by('-adddate')
    else:
        stories = Story.objects.all().order_by('-adddate')
    paginator = Paginator(stories, 20)
    page = request.GET.get('page')
    stories = paginator.get_page(page)
    story_cat = StoryCategory.objects.all()

    context = {'stories' : stories, 'time': datetime.now(), 'story_cat': story_cat}
    return render(request, 'stories.html', context)

@login_required(login_url='signin')
def mystories(request):
    if request.user.is_authenticated:
        stories = Story.objects.filter(uid=request.user).order_by('-adddate')
        paginator = Paginator(stories, 20)
        page = request.GET.get('page')
        stories = paginator.get_page(page)
        
        story_cat = StoryCategory.objects.all()
        context = {'stories' : stories, 'time': datetime.now(), 'title' : 'MyStories', 'story_cat': story_cat}
        return render(request, 'mystories.html', context)
    else:
        return redirect('/signin/?next=/create-story/')

#@login_required(login_url='signin')
def story_page(request, pk):
    story = get_object_or_404(Story, pk=pk)
    title = story.title
    story_cat = StoryCategory.objects.all()

    story_item = Story.objects.all()
    len_story = len(story_item)
    if len_story > 4 :
        random_story =  random.sample(list(story_item), 5)
    else :
        random_story =  random.sample(list(story_item), len_story)

    if request.method == 'POST':
        user_id = request.user
        comment_post = request.POST['comment']
        comment = StoryComment(sid=story, uid=user_id, comment=comment_post)
        comment.save()
        return redirect(reverse('story-detail', args=[pk]))

    context = { 'story': story , 'story_cat' : story_cat, 'random_story' : random_story, 'title' : title }
    return render(request, 'story-page.html', context)    

@login_required(login_url='signin')
def create_story(request):
    #if request.user.is_authenticated:
    if request.method == 'POST' and request.FILES['thumbnail']:
        user_id = request.user
        title = request.POST['title']
        thumbnail = request.FILES['thumbnail']
        category = request.POST['category']
        content = request.POST['content']
        cat = StoryCategory.objects.get(id=category)
        story = Story(uid=user_id, title=title, category=cat, thumb=thumbnail, content=content)
        story.save()

        sc_list = StoryCategory.objects.all()
        story_form=StoryForm()
        context = {'story_form':story_form, 'sc_list' : sc_list}

        return render(request, 'create-story.html', context)
    else:
        story_form=StoryForm()
        sc_list = StoryCategory.objects.all()
        context = {'story_form':story_form, 'sc_list' : sc_list}

        return render(request,'create-story.html',context)
    #else:
    #    return redirect('/signin/?next=/create-story/')

def story_category(request, slug):
    stories = get_list_or_404(Story.objects.order_by('-adddate'), category__slug=slug)
    category = StoryCategory.objects.get(slug=slug)

    archive_title = 'Story Category : ' + category.name 
    story_cat = StoryCategory.objects.all()

    context = {'stories' : stories, 'archive_title': archive_title, 'story_cat' :  story_cat}
    return render(request, 'story-archive.html', context)

