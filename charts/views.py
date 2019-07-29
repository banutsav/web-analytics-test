import pandas as pd
from django.shortcuts import render
from . import viz
from charts.models import EblityTopicTable

# Create your views here.
def index_page(request):
	# Get Topic data for Grade 8
	topics = pd.DataFrame(list(EblityTopicTable.objects.filter(grade=8).order_by('sequence')
		.values_list('topic_name','sequence','month','hours', 'weightage',named=True)))
	# Create figure from data
	fig = viz.createScatter(topics) 
	return render(request,'charts/index.html',{'fig':fig})