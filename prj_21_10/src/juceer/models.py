from django.conf import settings
from django.db import models
from django.utils import crypto

User = settings.AUTH_USER_MODEL

class JuceerPost(models.Model):
	song_id = models.SlugField(unique = True, default = crypto.get_random_string(length = 5))
	artist_hotttnesss= models.FloatField(default = 0)
	artist_id = models.CharField(max_length=100, default = crypto.get_random_string(length = 5))
	artist_name = models.CharField(max_length=100, default = crypto.get_random_string(length = 5))
	artist_terms = models.CharField(max_length=100, default = crypto.get_random_string(length = 5))
	release_id = models.IntegerField(default = 0)
	song_hotttnesss= models.FloatField(default = 0)
	song_year = models.IntegerField(default = 0)
