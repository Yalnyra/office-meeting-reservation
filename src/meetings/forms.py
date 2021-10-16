from django import forms
from django.utils.datetime_safe import time

from rooms.models import Room
from .models import Meeting

class MeetingForm(forms.Form):
    reserved_room = forms.ModelChoiceField(label='Reserved room', queryset=Room.objects.all(),
                                           widget=forms.Select(attrs={'class': 'form-control js-example-basic-single'}))
    time_start = forms.DateTimeField(label='Start time', widget=forms.DateTimeField(attr={'class': 'form-control'}))
    time_end = forms.DateTimeField(label='End time', widget=forms.DateTimeField(attr={'class': 'form-control'}))

    def clean(self, *args, **kwargs):
        data = self.cleaned_data()

        if data['time_end'] <= data['time_start']:
            raise forms.ValidationError('Meeting must start after its beginning')
        if data['time_start'] <= time.time():
            raise forms.ValidationError('Meeting must be scheduled before it will start')
        return data['time_end']


