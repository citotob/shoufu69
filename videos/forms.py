from django import forms
from videos.models import Video

class VideoForm(forms.ModelForm):
    #videofile = forms.FileField() 
    #progressbar = forms.ProgressBarField(link_to=videofile)
    class Meta:
        model= Video
        fields= ["title", "description", "tags", "category", "videofile"]

    def __init__(self, *args, **kwargs):
        super(VideoForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
