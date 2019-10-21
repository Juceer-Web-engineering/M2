from django.conf import settings
from django.db import models
from django.utils import crypto

User = settings.AUTH_USER_MODEL

class JuceerPostQuerySet(models.QuerySet):
	def published(self):
		now = timezone.now()
		return self.filter(publish_date__lte = now)
	def search(self,query):
		return self.filter(title__iexact = query)

class JuceerPostManager(models.Manager):
	def get_queryset(self):
		return JuceerPostQuerySet(self.model, using = self._db)
	
	def published(self):
		return self.get_queryset().published()

	def search(self, query = None):
		if query is None:
			return self.get_queryset().none()
		return self.get_queryset().search(query)


class JuceerPost(models.Model):
	song_id = models.SlugField(unique = True, default = crypto.get_random_string(length = 5))
	artist_hotttnesss= models.FloatField(default = 0)
	artist_id = models.CharField(max_length=100, default = crypto.get_random_string(length = 5))
	artist_name = models.CharField(max_length=100, default = crypto.get_random_string(length = 5))
	artist_terms = models.CharField(max_length=100, default = crypto.get_random_string(length = 5))
	release_id = models.IntegerField(default = 0)
	song_hotttnesss= models.FloatField(default = 0)
	song_year = models.IntegerField(default = 0)
