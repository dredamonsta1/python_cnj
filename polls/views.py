from django.shortcuts import render
from django.http import HttpResponse



def index(request):
	return HttpResponse("Hello, world. your at polls index. polls/view.")

# Create your views here.
