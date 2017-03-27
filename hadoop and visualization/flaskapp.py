from flask import Flask, request, session, redirect, url_for, make_response, send_file, render_template,send_from_directory
from subprocess import call
import pygal
from decimal import *
import pandas as pd
from pygal.style import DarkGreenBlueStyle
global CHART_NAME
CHART_NAME=''
app = Flask(__name__)


@app.route('/',methods = ['POST', 'GET'])
def hello_world():  
    if request.method == 'POST':
	CHART_NAME=request.form['charts']
	return redirect(url_for('.hadoop', CHART_NAME=CHART_NAME))	
    return '''
	<html>
	<head><title>Hadoop</title></head>
	<body>
	<p>Select the type of report and trigger the job!</p>
	<form action='' method='POST'>
	<select name="charts">
    	<option value="line_chart">Line</option>
    	<option value="bar_chart">Bar</option>
    	<option value="pie_chart">Pie</option>
 	 </select> 
	<input type="submit" value='Trigger Job'/>
	</form>
	</body>
	</html>'''

@app.route('/hadoop')
def hadoop():
	key = request.args.get("CHART_NAME")
	call(['bash', '/home/hduser/script/test.sh'])
	call(['bash', '/home/hduser/script/sample.sh'])
	return redirect(url_for('.report',CHART_NAME=key))


@app.route('/report')
def report():
        try:
            graph = pd.read_csv(r'/home/hduser/files/sample.csv')
	    key = request.args.get("CHART_NAME")
            #graph = graph.sort_values(by='count',ascending=False)
	    
	    if(key=='bar_chart'):
            	bar_chart = pygal.Bar(style=DarkGreenBlueStyle, width=1280, height=720, legend_at_bottom=True, human_readable=False, title='earthquake_bar')
	    elif(key=='line_chart') :
            	line_chart = pygal.Line(style=DarkGreenBlueStyle, width=1280, height=720, legend_at_bottom=True, human_readable=False, title='earthquake_pie')
	    else:
		pie_chart = pygal.Pie(style=DarkGreenBlueStyle, width=1280, height=720, legend_at_bottom=True, human_readable=False, title='earthquake_line')
            #scatter_chart = pygal.XY(stroke=False,style=DarkGreenBlueStyle, width=1280, height=720, legend_at_bottom=False, human_readable=True, title='earthquake_scatter')
	    
            if(key == 'bar_chart'):
            	for index, row in graph.iterrows():
			
                	bar_chart.add(str(row["place"]), (row["jan"], row["feb"], row["mar"], row["apr"], row["may"], row["jun"], row["jul"], row["aug"], row["sep"], row["oct"], row["nov"],row["dec	"]))
            elif (key=='line_chart'):
		for index, row in graph.iterrows():
			

			line_chart.add(str(row["place"]), (row["jan"], row["feb"], row["mar"], row["apr"], row["may"], row["jun"], row["jul"], row["aug"], row["sep"], row["oct"], row["nov"], row["dec	"]))

	    else:
		for index, row in graph.iterrows():
			

			pie_chart.add(str(row["place"]), (row["jan"], row["feb"], row["mar"], row["apr"], row["may"], row["jun"], row["jul"], row["aug"], row["sep"], row["oct"], row["nov"], row["dec	"]))


                #scatter_chart.add("", [(row["date"],row["count"])])
                #line_chart.add(str(row["date"]),row["count"])
		
            if(key == 'bar_chart'):
            	bar_chart.render()
	    elif(key=='line_chart'):
		line_chart.render()
	    else:
            	pie_chart.render()
            
            #scatter_chart.render_to_file('images/earthquakes_scatter.svg')
	    if(key == 'bar_chart'):
            	graph_data = bar_chart.render_data_uri()
	    elif(key=='line_chart'):
		graph_data = line_chart.render_data_uri()
	    else:
		graph_data = pie_chart.render_data_uri()

            return render_template("graphing.html", graph_data = graph_data)
        except Exception, e:
                return(str(e))

if __name__ == '__main__':
    app.run(host='0.0.0.0')