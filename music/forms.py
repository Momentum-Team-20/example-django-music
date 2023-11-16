from .models import Album, Artist
from django import forms


class AlbumForm(forms.ModelForm):
    artist_name = forms.CharField(max_length=255)

    class Meta:
        model = Album
        fields = ("title", "artist_name", "release_date", "genres")
