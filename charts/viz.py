import plotly.express as px
import plotly.offline as opy

def createScatter(topics):
	#print(topics['month'].unique())
	fig = px.scatter(topics, x='sequence', y='month', size='hours', color='weightage')
	plot = opy.plot(fig, auto_open=False, output_type='div', include_plotlyjs=False)
	return plot