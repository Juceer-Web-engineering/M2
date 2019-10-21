import csv, io
import logging
from django.contrib import messages
from django.contrib.auth.decorators import permission_required, login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.admin.views.decorators import staff_member_required

from .models import JuceerPost
from .forms import JuceerPostModelForm

import statistics 
import numpy as np

def artist_detail_view (request, artist_id):			#shows a details about given artist
	qs = JuceerPost.objects.filter(artist_id = artist_id).all()
	qs_list = list(JuceerPost.objects.filter(artist_id = artist_id).values_list('song_hotttnesss', flat=True))
	qs_year = list(JuceerPost.objects.filter(artist_id = artist_id).values_list('song_year', flat=True).distinct())
	qs_year = sorted(qs_year)

	numb = len(qs_list)
	if(numb > 1):
		std_deviation = statistics.stdev(qs_list)
	else:
		std_deviation = 0

	stat = [] 
	list_year = []

	for i in range(len(qs_year)):
		list_year = list(JuceerPost.objects.filter(artist_id = artist_id).filter(song_year = qs_year[i]).values_list('song_hotttnesss', flat=True))
		stat.append('\t' + str(qs_year[i]))
		stat.append("Mean: "+ str(statistics.mean(qs_list)))
		stat.append("Median: " +  str(statistics.median(qs_list)))
		if(len(list_year)>1):
			stat.append("Standart deviation: " + str(statistics.stdev(qs_list)))
		else:
			stat.append("Standart deviation: 0")

	

	template_name = 'juceer/detail_artist.html'
	context = {"object": qs[0], "number": numb, "mean": statistics.mean(qs_list), "median": statistics.median(qs_list), "std_deviation": std_deviation, "stat": stat}
	return render(request, template_name, context)


def artist_list_view (request):							#shows a list of artists sorted in alphabet order (distinct)
	#qs = JuceerPost.objects.order_by('artist_name').values('artist_name').distinct()
	qs = JuceerPost.objects.order_by('artist_name')
	template_name = 'juceer/list.html'
	context = {"object_list": qs, "title": "Artists"}
	return render(request, template_name, context)

def artist_genre_list_view (request):					#shows a list of artists sorted by genre 
	qs = JuceerPost.objects.order_by('artist_name').order_by('artist_terms').values('artist_name').distinct()			
	template_name = 'juceer/list.html'
	context = {"object_list": qs, "title": "Artists by genre"}
	return render(request, template_name, context)

def artist_popularity_list_view (request, number):				#shows a list of artists sorted by popularity
	qs = JuceerPost.objects.order_by('artist_name').order_by('artist_hotttnesss').reverse()				
	template_name = 'juceer/list.html'
	if(number == 'all'):
		qs = qs
	else: 
		qs = qs[:int(number)]
	context = {"object_list": qs, "title": "Artists by popularity"}
	return render(request, template_name, context)



def genre_list_view (request):					#shows a list of artists sorted by genre 
	qs = JuceerPost.objects.values_list('artist_terms', flat=True).order_by('artist_terms').distinct()
	qs_list = list(qs)
	template_name = 'juceer/list_search.html'
	context = {"object_list": qs_list, "title": "Genres"}
	return render(request, template_name, context)



def years_list_view (request):					#shows a list of artists sorted by genre 
	qs = JuceerPost.objects.values_list('song_year', flat=True).order_by('song_year').distinct().reverse()
	qs_list = list(qs)
	print(qs_list)			
	template_name = 'juceer/list_search.html'
	context = {"object_list": qs_list, "title": "Genres"}
	return render(request, template_name, context)



def song_artist_list_view (request, artist_id):				#shows a list of songs of artist sorted by popularity
	qs = JuceerPost.objects.filter(artist_id = artist_id).order_by('song_hotttnesss')
	template_name = 'juceer/list_song.html'
	context = {"object_list": qs, "title": qs[0].artist_name}
	return render(request, template_name, context)

def song_popularity_list_view (request):				#shows a list of songs sorted by popularity
	qs = JuceerPost.objects.order_by('song_id').order_by('song_hotttnesss')
	template_name = 'juceer/list_song.html'
	context = {"object_list": qs, "title": " by popularity"}
	return render(request, template_name, context)

def song_year_view (request):							#shows a list of songs sorted by year
	qs = JuceerPost.objects.order_by('song_id').order_by('song_year')					
	template_name = 'juceer/list_song.html'
	context = {"object_list": qs, "title": " by year"}
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
		"title": "Song",
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

@staff_member_required
def post_delete_view (request, song_id):				#delete the entry
	obj = get_object_or_404(JuceerPost, song_id = song_id)
	template_name = 'juceer/delete.html'
	if(request.method== "POST"):
		obj.delete()
		return redirect("/juceer")
	context = {"object": obj}
	return render(request, template_name, context)

@staff_member_required
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

		