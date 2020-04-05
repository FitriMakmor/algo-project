import dash
import dash_core_components as dcc
import dash_html_components as html

app= dash.Dash()

app.title = 'Word Count'

app.layout=html.Div(
    html.Div([
        html.H1(children='Word and Stop Count'),

        dcc.Graph(
            id='example-graph',
            figure={
                'data': [
                    {'x':['Beijing','Hong Kong','Indonesia','Japan','Korea','Taiwan','Thailand'],'y':[4033,4019,2619,3233,2338,3861,2764],'type':'bar','name':'Word Count' },
                    {'x':['Beijing','Hong Kong','Indonesia','Japan','Korea','Taiwan','Thailand'],'y':[1456,1360,825,1092,845,1320,977],'type':'bar','name': 'Stop Count'}
                ],
                'layout':{
                    'title':'Positive and Negative Words'
                }
            }
        ),

])
)


if __name__ == '__main__':
    app.run_server(debug=True, port=3007)
