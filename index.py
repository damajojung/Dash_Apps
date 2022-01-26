
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Connect to main app.py file
from app import app
from app import server

# Connect to your app pages
from apps import test, tf_idf_avg_plot , heatmap, LDA_Plot, scattertext


app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div([
        dcc.Link('  Test  |', href='/apps/test'),
        dcc.Link('  TF.IDF LinePlot  |', href='/apps/tf_idf_avg_plot'),
        dcc.Link('  HEATMAP  |', href='/apps/heatmap'),
        dcc.Link('  LDA Plot  |', href='/apps/LDA_Plot'),
        dcc.Link('  Scattertext  |', href='/apps/scattertext')
    ], className="row"),
    html.Div(id='page-content', children=[])
])


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])

def display_page(pathname):
    if pathname == '/apps/test':
        return test.layout
    if pathname == '/apps/tf_idf_avg_plot':
        return tf_idf_avg_plot.layout
    if pathname == '/apps/heatmap':
        return heatmap.layout
    if pathname == '/apps/LDA_Plot':
        return LDA_Plot.layout
    if pathname == '/apps/scattertext':
        return scattertext.layout
    else:
        return "Please choose a link"


if __name__ == '__main__':
    app.run_server(debug=False)



#     http://127.0.0.1:8050/

