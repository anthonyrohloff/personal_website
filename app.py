from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
import dash

app = Dash(
    __name__,
    suppress_callback_exceptions=True,
    external_stylesheets=[dbc.themes.MATERIA, dbc.icons.FONT_AWESOME, 'assets/sidebar.css', 'assets/body.css', 'assets/header.css', 'assets/typography.css'],
    use_pages=True
)

sidebar = html.Div(
    [
        html.Div(
            [
                html.H2("Navigation", style={"color": "#BFCBCE"}),
            ],
            className="sidebar-header",
        ),
        dbc.Nav(
            [
                dbc.NavLink(
                    [
                        html.Div([
                            html.I(className="fas fa-home me-2"),
                            html.Span("Home", style={"color": "#BFCBCE", "verticalAlign": "middle"})
                        ], className="d-flex align-items-center")
                    ],
                    href="/",
                    active="exact",
                    className="nav-link",
                ),
                html.Br(),
                dbc.NavLink(
                    [
                        html.Div([
                            html.I(className="fas fa-user me-2"),
                            html.Span("Blog", style={"color": "#BFCBCE", "verticalAlign": "middle"})
                        ], className="d-flex align-items-center")
                    ],
                    href="/blog",
                    active="exact",
                    className="nav-link",
                ),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    className="sidebar",
)

app.layout = html.Div([
    sidebar,
    html.H1('Multi-page app with Dash Pages'),
    html.Div([
        html.Div(
            dcc.Link(f"{page['name']} - {page['path']}", href=page["relative_path"])
        ) for page in dash.page_registry.values()
    ]),
    dash.page_container
])

if __name__ == '__main__':
    app.run_server(debug=True)
