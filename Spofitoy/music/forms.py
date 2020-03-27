from django import forms
from .models import Artist

class ArtistForm(forms.ModelForm):
    """
    Artist form model
    """

    class Meta:
        model = Artist
        fields = ('name',)