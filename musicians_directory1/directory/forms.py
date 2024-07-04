from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Musician, Album

class MusicianForm(forms.ModelForm):
    class Meta:
        model = Musician
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'instrument_type']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Save'))

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['musician', 'album_name', 'release_date', 'rating']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Save'))
