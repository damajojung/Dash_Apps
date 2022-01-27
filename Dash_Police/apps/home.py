from dash import html
import dash_bootstrap_components as dbc

# needed only if running this as a single page app
external_stylesheets = [dbc.themes.LUX]

#app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# change to app.layout if running as single page app instead
layout = html.Div([
    dbc.Container([
        dbc.Row([
            dbc.Col(html.H1("DSP Police Academy", className="text-center")
                    , className="mb-5 mt-5")
        ]),
        dbc.Row([
            dbc.Col(html.H5(children='This is a project for the University of Amsterdam, in cooperation with the Police Academy, and the Dutch Organisation for applied scientific research (TNO). '
                                     )
                    , className="mb-4")
            ]),

        dbc.Row([
            dbc.Col(html.P(children='The aim of this project is to provide an analysis tool to extract the Modus Operandi of criminals. '
                                     'Refer to the About page for more information about the project.')
                        , className="mb-5"),
        ]),

        dbc.Row([
            dbc.Col(dbc.Card(children=[html.H3(children='Access the code and datasets.',
                                               className="text-center"),
                                       dbc.Button("GitHub",
                                                  href="https://github.com/Lizzydrb/DSP_Police_Academy",
                                                  color="primary",
                                                  className="d-grid gap-2 col-6 mx-auto"),
                                       ],
                             body=True, color="dark", outline=True)
                    , width=4, className="mb-4"),

            dbc.Col(dbc.Card(children=[html.H3(children='Read our final report.',
                                               className="text-center"),
                                       dbc.Button("Title...",
                                                  href="https://medium.com/@meredithwan",
                                                  color="primary",
                                                  className="d-grid gap-2 col-6 mx-auto"),

                                       ],
                             body=True, color="dark", outline=True)
                    , width=4, className="mb-4")
        ], className="mb-5"),

        html.A("Special thanks to ....",
               href="https://www.flaticon.com/free-icon/coronavirus_2913604")

    ])

])

# needed only if running this as a single page app
# if __name__ == '__main__':
#     app.run_server(host='127.0.0.1', debug=True)