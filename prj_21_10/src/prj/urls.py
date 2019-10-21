from django.contrib import admin
from django.urls import path, re_path, include 
from juceer.views import post_create_view

from searches.views import search_view
from .views import (home_page, about_page)

urlpatterns = [
	path('', home_page),
	path('about/', about_page),
    path('admin/', admin.site.urls),
            #urls connected to Juceer app 
    path('juceer-new/', post_create_view),	#to avoid problems with juceer/<str:slug>/ we use another naming (not blog/create)
	path('juceer/', include('juceer.urls')),
	path('search/', search_view),

]
