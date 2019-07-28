import plotly.express as px
import plotly.offline as opy

def createScatter():
	gapminder = px.data.gapminder()
	gapminder2007 = gapminder.query("year == 2007")
	fig = px.scatter(gapminder2007, x='gdpPercap', y='lifeExp')
	plot = opy.plot(fig, auto_open=False, output_type='div', include_plotlyjs=False)
	return plot