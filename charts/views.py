from django.shortcuts import render
from . import viz
# Create your views here.

def index_page(request):
	fig = viz.createScatter() 
	return render(request,'charts/index.html',{'fig':fig})