
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Connect to main app.py file
from app import app
from app import server

# Connect to your app pages
from apps import vgames, global_sales, test, tf_idf_avg_score


app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div([
        dcc.Link('Video Games  |', href='/apps/vgames'),
        dcc.Link('  Other Products  |', href='/apps/global_sales'),
        dcc.Link('  Test  |', href='/apps/test'),
        dcc.Link('  Test  |', href='/apps/tf_idf_avg_plot')
    ], className="row"),
    html.Div(id='page-content', children=[])
])


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])

def display_page(pathname):
    if pathname == '/apps/vgames':
        return vgames.layout
    if pathname == '/apps/global_sales':
        return global_sales.layout
    if pathname == '/apps/test':
        return test.layout
    if pathname == '/apps/tf_idf_avg_plot':
        return tf_idf_avg_plot.layout
    else:
        return "404 Page Error! Please choose a link"


if __name__ == '__main__':
    app.run_server(debug=False)



#     http://127.0.0.1:8050/

