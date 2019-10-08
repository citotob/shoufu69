# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect

from django.http import HttpResponse
from stories.forms import StoryForm
from .models import StoryCategory, Story

import random

def stories(request):
    stories = Story.objects.all().order_by('-adddate')
    story_cat = StoryCategory.objects.all()
    context = {'stories' : stories, 'story_cat': story_cat}
    return render(request, 'stories.html', context)

def story_page(request, pk):
    story = get_object_or_404(Story, pk=pk)
    story_cat = StoryCategory.objects.all()

    story_item = Story.objects.all()
    len_story = len(story_item)
    if len_story > 4 :
        random_story =  random.sample(list(story_item), 5)
    else :
        random_story =  random.sample(list(story_item), len_story)

    context = { 'story': story , 'story_cat' : story_cat, 'random_story' : random_story }
    return render(request, 'story-page.html', context)    

def create_story(request):
    if request.user.is_authenticated:
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
    else:
        return redirect('/signin/?next=/create-story/')

