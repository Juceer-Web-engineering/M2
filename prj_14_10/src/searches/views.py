from django.shortcuts import render

from juceer.models import JuceerPost

from .models import SearchQuery


# application for making searches in the database and keep on track every search of evey user.

def search_view(request):
	query = request.GET.get('q', None)
	user = None
	if request.user.is_authenticated:
		user = request.user
	context = {"query": query}
	if query is not None:	
		SearchQuery.objects.create(user = user, query = query)
		s_list = JuceerPost.objects.filter(artist_name__icontains = str(query)).all()|JuceerPost.objects.filter(artist_terms__icontains = str(query)).all()|JuceerPost.objects.filter(song_year__icontains = str(query))
		s_list = s_list.order_by('artist_name').all()
		context["s_list"] = s_list
	return render( request, 'searches/view.html', context)