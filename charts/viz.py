import plotly.express as px
import plotly.offline as opy

def createScatter(topics):
	fig = px.scatter(topics, x='sequence', y='hours', color='month')
	plot = opy.plot(fig, auto_open=False, output_type='div', include_plotlyjs=False)
	return plot