from django import forms
from .models import Story
from ckeditor.widgets import CKEditorWidget

class StoryForm(forms.ModelForm):
    title = forms.CharField(required=True)
    category = forms.ChoiceField(required=True)
    content = forms.CharField(widget=CKEditorWidget())
    thumb = forms.ImageField(required=True)

    class Meta:
        model = Story
        fields = ['title','category','content', 'thumb']