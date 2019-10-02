# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse
from .forms import StoryForm
from .models import StoryCategory

def create_story(request):

    story_form=StoryForm()
    sc_list = StoryCategory.objects.all()
    context = {'story_form':story_form, 'sc_list' : sc_list}

    return render(request,'create-story.html',context)