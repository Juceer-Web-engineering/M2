from django import forms
import uuid 

from .models import JuceerPost

class JuceerPostForm(forms.Form):
	song_id = forms.SlugField()
	artist_hotttnesss = forms.FloatField()
	artist_id = forms.CharField(max_length=100)
	artist_name = forms.CharField(max_length=100)
	artist_terms = forms.CharField(max_length=100)
	release_id = forms.IntegerField()
	song_hotttnesss= forms.FloatField()
	song_year = forms.IntegerField()

class JuceerPostModelForm(forms.ModelForm):
	class Meta:
		model = JuceerPost
		fields = [ 'artist_hotttnesss', 'artist_id', 'artist_name', 'artist_terms','release_id','song_hotttnesss','song_id', 'song_year']
	