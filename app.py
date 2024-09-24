from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
import dash

# Code to add a blogpost link in the sidebar, don't think I'll use
# def add_blogpost(url, name):
#     link = dbc.NavLink(
#                 [
#                     html.Div([
#                         html.I(className="fas fa-asterisk"),
#                         html.Span(name, style={"color": "#BFCBCE", "verticalAlign": "middle"})
#                     ], className="d-flex align-items-center")
#                 ],
#                 href=url,
#                 active="exact",
#                 className="nav-link",
#             )
#     return link

app = Dash(
    __name__,
    suppress_callback_exceptions=True,
    external_stylesheets=[dbc.themes.MATERIA, dbc.icons.FONT_AWESOME, 'assets/sidebar.css', 'assets/body.css', 'assets/header.css', 'assets/typography.css'],
    use_pages=True
)

server = app.server

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
                            html.I(className="fas fa-pencil"),
                            html.Span("Blog", style={"color": "#BFCBCE", "verticalAlign": "middle"})
                        ], className="d-flex align-items-center")
                    ],
                    href="/blog",
                    active="exact",
                    className="nav-link",
                )
            ],
            vertical=True,
            pills=True,
        ),
    ],
    className="sidebar",
)

app.layout = (
    sidebar,
    html.Div(
    className="app-header",
    children=[
    html.H1('anthonyrohloff.com'),
    dash.page_container
]))

if __name__ == '__main__':
    app.run_server(debug=True)
