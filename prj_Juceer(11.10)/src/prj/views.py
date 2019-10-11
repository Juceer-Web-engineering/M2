from django.http import HttpResponse 
from django.shortcuts import render
from django.template.loader import get_template

from .forms import ContactForm

def home_page(request):						# home page
	my_title = "We are happy to see you here! (Or whatever should be written on home page)"
	context ={"title": my_title}
	return render (request, "home.html", context)

def about_page(request):
	return render (request, "about_page.html")
