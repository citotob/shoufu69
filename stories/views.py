# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import redirect

from django.http import HttpResponse
from stories.forms import StoryForm
from .models import StoryCategory, Story

def stories(request):
    stories = Story.objects.all().order_by('-adddate')
    context = {'stories' : stories}
    return render(request, 'stories.html', context)

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

