import csv, io
import logging
from django.contrib import messages
from django.contrib.auth.decorators import permission_required

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

from .models import JuceerPost
from .forms import JuceerPostModelForm

def artist_detail_view (request, artist_id):			#shows a list of the songs of given artist
	qs = JuceerPost.objects.filter(artist_id = artist_id)
	template_name = 'juceer/list_song.html'
	context = {"object_list": qs, "title": "of songs of " + get_object_or_404(JuceerPost, artist_id = artist_id).artist_name}
	return render(request, template_name, context)

def artist_list_view (request):							#shows a list of artists sorted in alphabet order
	qs = JuceerPost.objects.order_by('artist_name')					
	template_name = 'juceer/list.html'
	context = {"object_list": qs, "title": "Artists"}
	return render(request, template_name, context)

def artist_genre_list_view (request):					#shows a list of artists sorted by genre (WILL BE CHANGED FOR MORE USER FRIENDLY)
	qs = JuceerPost.objects.order_by('artist_name').order_by('artist_terms')					
	template_name = 'juceer/list.html'
	context = {"object_list": qs, "title": "Artists by genre"}
	return render(request, template_name, context)

def artist_popularity_list_view (request):				#shows a list of artists sorted by popularity
	qs = JuceerPost.objects.order_by('artist_name').order_by('artist_hotttnesss')			
	template_name = 'juceer/list.html'
	context = {"object_list": qs, "title": "Artists by popularity"}
	return render(request, template_name, context)

def song_popularity_list_view (request):				#shows a list of songs sorted by popularity
	qs = JuceerPost.objects.order_by('song_id').order_by('song_hotttnesss')
	template_name = 'juceer/list_song.html'
	context = {"object_list": qs, "title": "Songs by popularity"}
	return render(request, template_name, context)

def song_year_view (request):							#shows a list of songs sorted by year
	qs = JuceerPost.objects.order_by('song_id').order_by('song_year')					
	template_name = 'juceer/list_song.html'
	context = {"object_list": qs, "title": "Songs by year"}
	return render(request, template_name, context)

def post_list_view (request):							#shows a list of artists in chronological order
	qs = JuceerPost.objects.order_by('artist_name')
	template_name = 'juceer/list.html'
	context = {"object_list": qs, "title": ""}
	return render(request, template_name, context)

@staff_member_required
def post_create_view (request):							#create a new entry
	form = JuceerPostModelForm(request.POST or None)
	if form.is_valid():
		print(form.cleaned_data)
		obj = form.save(commit = False)
		obj.save()
		form = JuceerPostModelForm()
	context = {
		"title": "Contact",
		"form": form
	}
	template_name = 'form.html'
	return render(request, template_name, context)

@staff_member_required
def post_detail_view (request, song_id):				#shows details about song
	obj = get_object_or_404(JuceerPost, song_id = song_id)
	template_name = 'juceer/detail.html'
	context = {"object": obj}
	return render(request, template_name, context)

@staff_member_required
def post_update_view (request, song_id):				#update the details about song
	obj = get_object_or_404(JuceerPost, song_id = song_id)
	form = JuceerPostModelForm(request.POST or None, instance = obj)
	if form.is_valid():
		form.save()
	template_name = 'form.html'
	context = {"form": form, "title": "Update"} 
	return render(request, template_name, context)

def post_delete_view (request, song_id):				#delete the entry
	obj = get_object_or_404(JuceerPost, song_id = song_id)
	template_name = 'juceer/delete.html'
	if(request.method== "POST"):
		obj.delete()
		return redirect("/juceer")
	context = {"object": obj}
	return render(request, template_name, context)


#@permission_required('admin.can_add_log_entry')
def song_upload(request):								#upload csv dataset (WILL BE FIXED)
	template = "uploading.html"
	prompt = {
		'order': 'work'
	}
	if request.method == "GET":
		return render(request, template, prompt)
	csv_file = request.FILES['file']
	dataset = csv_file.read().decode('UTF-8')
	io_string = io.StringIO(dataset)
	next(io_string)
	for column in csv.reader(io_string, delimiter = ',', quotechar="|"):

		_, created = JuceerPost.objects.update_or_create(
      		artist_hotttnesss= column[1],
			artist_id = column[2],
			artist_name = column[6],
			artist_terms = column[8],
			release_id = column[10],
			song_hotttnesss= column[20],
			song_id = column[21],
			song_year = column[34],
			)
		content = {}
	return render(request, template, content)
	#return HttpResponseRedirect(reverse("upload_csv"))

		