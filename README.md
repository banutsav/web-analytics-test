# web-analytics-test
Test web application to trial plotting, dashboards and visualizations. 
## Plotly charts in Django web pages
[Plotly](https://plot.ly/python/) is a powerful plotting library which works with Python and Javascript. 
This would need to be installed in your virtual environment, along with [Pandas](https://pandas.pydata.org/) and [Numpy](https://numpy.org/)
The relevant files to look at in this case are
```
charts/views.py
charts/viz.py
charts/index.html
```
### viz.py
The query dataset is fed into a method which uses plotly express to generate a scatter plot
```python
fig = px.scatter(topics, x='sequence', y='month', size='hours', color='weightage')
plot = opy.plot(fig, auto_open=False, output_type='div', include_plotlyjs=False)
return plot
```
The plot is returned as an HTML div object. The Plotly Javascript libraries are not included within it but will be pulled into the HTML page.
### views.py
The plot div object is called from the list of views. A query data set is passed to it after conversion into a dataframe.
```python
from django.shortcuts import render
from . import viz
# Create your views here.
def index_page(request):
	# Get Topic data for Grade 8
	topics = pd.DataFrame(list(EblityTopicTable.objects.filter(grade=8).order_by('sequence')
		.values_list('topic_name','sequence','month','hours', 'weightage',named=True)))
	fig = viz.createScatter() 
	return render(request,'charts/index.html',{'fig':fig})
```
This is passed in to the render using the ```fig``` variable, in this case for the index page
### index.html
The ```fig``` variable is displayed on the index page. The ```https://cdn.plot.ly/plotly-latest.min.js``` link gets the plotly libraries.
``` html
  <head>
    <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
    <title>Charts</title>
  </head>
  <body>
    {% autoescape off %}
      {{fig}}
    {% endautoescape %}
  </body>
```
The figure is printed within the ```autoescape``` tag otherwise the web-page renders it as a string and not as HTML.
