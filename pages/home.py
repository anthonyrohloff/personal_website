import dash
from dash import html

dash.register_page(__name__, path='/')

layout = html.Div([
    html.Br(),
    html.H2("About Me", style={"text-decoration": "underline"}),
    html.Div(
        "Hello!"
    ),
    html.Br(),
    html.Div(
        "My name is Anthony Rohloff, and I am a Cybersecurity Engineering student at the University of Cincinnati. I have minors in computer science and business administration. My studies are at the intersection of electrical engineering, computer engineering, and computer science."
    ),
    html.Br(),
    html.Div("Outside of school, I have also furthered my knowledge in the field of cybersecurity by earning two certifications. First, I earned SC-900, Microsoft Security, Identity, and Compliance Fundamentals. This certification helped me cement a strong foundation for essential cybersecurity concepts, as well as teach me about Microsoft-specific technologies such as Microsoft Entra and Sentinel. After that, I passed CompTIA Security+ SY0-701 on the first attempt. This certification is a highly popular certification for those trying to break into the industry due to its wide scope and application-oriented questions."),
    html.Br(),
    html.Div(
        "Additionally, I have experience as a controls engineering intern at BMW Manufacturing Co. in Spartanburg, South Carolina. In my department, I have had the opportunity to complete over 100 hours of professional development training, as well as work on technically-involved projects. These trainings and projects included topics such as Splunk, Profinet, Python, Power BI, and Agile work methodology."
    ),
    html.Br(),
    html.Div([
        "Please feel free to connect with me on ",
        html.A(
            [html.I(className="fa-brands fa-linkedin"), "LinkedIn"],
            href='https://www.linkedin.com/in/anthonyrohloff/',
            target="_blank"
        ),
        " for the most detailed and updated information about my education, professional experiences, and projects."
    ]),
    html.Br(),
    html.Br(),
    html.Br()
])