from django.urls import path, include
from .views import (post_list_view, post_delete_view, post_detail_view, post_update_view, 
					artist_detail_view, artist_list_view, artist_popularity_list_view,artist_genre_list_view,
					song_popularity_list_view, song_artist_list_view,
					genre_list_view,years_list_view)

from .views import (
	song_upload,
	)

urlpatterns = [
	path('artist/', artist_list_view),
	path('artist/genre/', artist_genre_list_view),
	path('artist/popularity/<str:number>/', artist_popularity_list_view),
	path('artist/<str:artist_id>/', artist_detail_view),
	path('artist/<str:artist_id>/song/',song_artist_list_view),
	
	path('song/popularity/', song_popularity_list_view),
	path('song/<str:song_id>/', post_detail_view),
	path('song/<str:song_id>/edit/', post_update_view),		
	path('song/<str:song_id>/delete/', post_delete_view),		

	path('genre/', genre_list_view),
	path('year/', years_list_view),

	path('upload-csv/', song_upload),
]



