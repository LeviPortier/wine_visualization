import plotly.graph_objects as go
import pandas as pd




def create_paracoords(data):
    fig = go.Figure(data=
                go.Parcoords(
                    line = dict(color = data['quality'], colorscale = [[3,'#0d0887'], [4,'#46039f'], [5,['#7201a8'], [6,'#9c179e'], [7,'#bd3786'], [8,'#d8576b'], [9,'#ed7953']]),dimensions = list([
                        dict(constraintrange = [7.5,9]
                             label = 'quality', values = data['quality']),
                        dict(label = 'alcohol', values = data['alcohol']),
                        dict(label = 'sulphates', values = data['sulphates']),
                        dict(label = 'pH', values = data['pH']),
                        dict(label = 'total sulfur dioxide', values = data['total sulfur dioxide']),
                        dict(label = 'density', values = data['density']),
                        dict(label = 'free sulfur dioxide', values = data['free sulfur dioxide']),
                        dict(label = 'chlorides', values = data['chlorides']),
                        dict(label = 'residual sugar', values = data['residual sugar']),
                        dict(label = 'citric acid', values = data['citric acid']),
                        dict(label = 'volatile acidity', values = data['volatile acidity']),
                        dict(label = 'fixed acidity', values = data['fixed acidity'])])))
    fig.update_layout(autosize=False,width=600,height=600, template='presentation')

    return fig
