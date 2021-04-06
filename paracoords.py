import plotly.graph_objects as go
import pandas as pd

def create_paracoords(data):
    fig = go.Figure(data=
                go.Parcoords(
                    line = dict(color = data['quality']),dimensions = list([
                        dict(constraintrange = [7.5,9],
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
    fig.update_layout(template='presentation')

    return fig