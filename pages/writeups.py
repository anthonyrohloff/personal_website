import dash
from dash import html, dcc, Dash
import os

# Manually enter each entry's information here
entry_info = {
    "entry1": {"name": "Simple CTF Write-up", "date": "September 27th, 2024"},
    "entry2": {"name": "Mr. Robot CTF Write-up", "date": "September 28th, 2024"},
    "entry3": {"name": "Crack the Hash Write-up", "date": "September 29th, 2024"},
    "entry4": {"name": "Library Write-up", "date": "September 30th, 2024"}
}

# Set up entry dict
entry_dict = {
    entry[:-3]: entry_info.get(entry[:-3], {"name": "not found", "date": "not found"})
    for entry in os.listdir(r"pages/writeups")
    if os.path.isfile(os.path.join(r"pages/writeups", entry))
}

dash.register_page(__name__)

layout = html.Div([
    html.H1("CTF Write-Ups"),
    html.Div(
        [
            html.Div([
                dcc.Link(entry_dict[entry]["name"], href=f"/writeups/{entry}"),
                html.Span(f" - {entry_dict[entry]['date']}") ,
                html.Br(),
        ]) for entry in entry_dict
        ]
    )
])