from .models import Job_seeker
from django import forms

class Seekerform(forms.ModelForm):
    class Meta:
        model = Job_seeker
        exclude = ['user']

    def __init__(self,*args, **kwargs):
        super(Seekerform, self).__init__(*args, **kwargs)
