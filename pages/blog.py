import dash
from dash import html, dcc, Dash
import os

# Manually enter each entry's information here
entry_info = {
    "entry1": {"name": "The Impending Impact of Quantum Computing on Encryption Algorithms", "date": "August 10th, 2024"},
}

# Set up entry dict
entry_dict = {
    entry[:-3]: entry_info.get(entry[:-3], {"name": "not found", "date": "not found"})
    for entry in os.listdir(r"pages/blog_entries")
    if os.path.isfile(os.path.join(r"pages/blog_entries", entry))
}

dash.register_page(__name__)

layout = html.Div([
    html.H1("Blog Entries"),
    html.Div(
        [
            html.Div([
                dcc.Link(entry_dict[entry]["name"], href=f"/blog/{entry}"),
                html.Span(f" - {entry_dict[entry]['date']}") ,
                html.Br(),
        ]) for entry in entry_dict
        ]
    )
])