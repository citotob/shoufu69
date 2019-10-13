# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse
from stories.forms import StoryForm
from .models import StoryCategory, Story
from datetime import datetime
from django.core.paginator import Paginator
import random

def stories(request):
    stories = Story.objects.all().order_by('-adddate')
    paginator = Paginator(stories, 20)
    page = request.GET.get('page')
    stories = paginator.get_page(page)
    context = {'stories' : stories, 'time': datetime.now()}
    return render(request, 'stories.html', context)

@login_required(login_url='signin')
def mystories(request):
    if request.user.is_authenticated:
        stories = Story.objects.filter(uid=request.user).order_by('-adddate')
        paginator = Paginator(stories, 20)
        page = request.GET.get('page')
        stories = paginator.get_page(page)
        context = {'stories' : stories, 'time': datetime.now(), 'title' : 'MyStories'}
        return render(request, 'mystories.html', context)
    else:
        return redirect('/signin/?next=/create-story/')

def story_page(request, pk):
    story = Story.objects.get(pk=pk)
    title = story.title
    story_cat = StoryCategory.objects.all()

    story_item = Story.objects.all()
    len_story = len(story_item)
    if len_story > 4 :
        random_story =  random.sample(list(story_item), 5)
    else :
        random_story =  random.sample(list(story_item), len_story)

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

