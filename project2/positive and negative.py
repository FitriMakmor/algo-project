import dash
import dash_core_components as dcc
import dash_html_components as html

app= dash.Dash()

app.tittle ='Positive word'

app.layout=html.Div(
    html.Div([
        html.H1(children='Graphs of positive and negative words found in the webpages.'),

        dcc.Graph(
            id='example-graph',
            figure={
                'data': [
                    {'x':['Beijing','Hong Kong','Indonesia','Japan','Korea','Taiwan','Thailand'],'y':[133,117,114,128,66,57,122],'type':'bar','name':'Negative Count' },
                    {'x':['Beijing','Hong Kong','Indonesia','Japan','Korea','Taiwan','Thailand'],'y':[64,57,33,48,46,78,57],'type':'bar','name': 'Positive Count'}
                ],
                'layout':{
                    'titlee':'Positive and negative word'
                }
            }
        ),

])
)



if __name__ =='__main__':
    app.run_server(debug=True,port=3006)
