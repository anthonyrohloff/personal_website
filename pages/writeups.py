import dash
from dash import html, dcc, Dash
import os

# Set up entry dict
entry_dict = {
    entry[:-3]: {"name": "", "date": ""}
    for entry in os.listdir(r"pages/writeups")
    if os.path.isfile(os.path.join(r"pages/writeups", entry))
}

# Set name and date for each entry, will have to be done manually for now
for key in entry_dict.keys():
    match key:
        case "entry1":
            entry_dict[key]["name"] = "Simple CTF Write-up"
            entry_dict[key]["date"] = "September 27th, 2024"

        case _:
            entry_dict[key]["name"] = "not found"
            entry_dict[key]["date"] = "not found"

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