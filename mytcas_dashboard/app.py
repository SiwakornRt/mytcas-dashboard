# Import packages
from dash import Dash, html, dcc, callback, Output, Input, dash_table
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
import json
import plotly.graph_objects as go
# from data.university import university_coords

# Load data from CSV file
data = pd.read_csv("data/data_mark_01.csv")
# Create DataFrame from CSV data
df = pd.DataFrame(data)
# df["lat"] = df["uni"].map(
#     lambda x: university_coords[x]["lat"] if x in university_coords else None
# )
# df["lon"] = df["uni"].map(
#     lambda x: university_coords[x]["lon"] if x in university_coords else None
# )

# Initialize the Dash app with a dark theme
app = Dash(external_stylesheets=[dbc.themes.DARKLY])

# URL for the Plotly logo
PLOTLY_LOGO = "https://images.plot.ly/logo/new-branding/plotly-logomark.png"

# Define the navigation bar
navbar = dbc.Navbar(
    dbc.Container(
        [
            html.A(
                dbc.Row(
                    [
                        dbc.Col(html.Img(src=PLOTLY_LOGO, height="30px")),
                        dbc.Col(dbc.NavbarBrand("Dashboard", className="ms-2")),
                    ],
                    align="center",
                    className="g-0",
                ),
                href="https://plotly.com",
                style={"textDecoration": "none"},
            ),
        ]
    ),
    color="dark",
    dark=True,
)

# Define the header section
header = html.Div(
    children=[
        html.H1(
            children="Number Of Admitted Dashboard 2566",
            style={
                "textAlign": "center",  # Center text horizontally
                "margin": "20px auto",  # Add margin to center the element horizontally
                "width": "100%",  # Make the H1 take the full width
            },
        ),
        html.P(
            children="Number of admitted from Mytcas website",
            style={
                "textAlign": "center",  # Center text horizontally
                "width": "100%",  # Make the paragraph take the full width
            },
        ),
    ]
)

# Create options for the university dropdown, including "Select All"
university_options = [{"label": "Select All", "value": "all"}] + [
    {"label": university, "value": university} for university in df["uni"].unique()
]

# Create options for the major dropdown, including "All"
major_options = [{"label": "Select All", "value": "all"}] + [
    {"label": major, "value": major} for major in df["major"].unique()
]

# Create options for the course dropdown, including "All"
course_options = [{"label": "Select All", "value": "all"}] + [
    {"label": course, "value": course} for course in df["course"].unique()
]

# Define the filter section with dropdowns for university, major, and sorting
filter = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(
                    html.Div(
                        [
                            html.H6(
                                "University", style={"marginBottom": "10px"}
                            ),  # Header for the university dropdown
                            dcc.Dropdown(
                                id="university-dropdown",
                                options=university_options,
                                value=["all"],  # Default value is "Select All"
                                multi=True,
                                style={
                                    "width": "100%",
                                    "color": "black",
                                    "backgroundColor": "white",
                                },
                            ),
                        ]
                    ),
                    width=6,
                    style={"padding": "0 10px"},
                ),
                dbc.Col(
                    html.Div(
                        [
                            html.H6(
                                "Major", style={"marginBottom": "10px"}
                            ),  # Header for the major dropdown
                            dcc.Dropdown(
                                id="major-dropdown",
                                options=major_options,
                                value="all",  # Default value is "All"
                                style={
                                    "width": "100%",
                                    "color": "black",
                                    "backgroundColor": "white",
                                },
                            ),
                        ]
                    ),
                    width=3,
                    style={"padding": "0 5px"},
                ),
                dbc.Col(
                    html.Div(
                        [
                            html.H6(
                                "Course", style={"marginBottom": "10px"}
                            ),  # Header for the course dropdown
                            dcc.Dropdown(
                                id="course-dropdown",
                                options=course_options,
                                value="all",  # Default value is "All"
                                style={
                                    "width": "100%",
                                    "color": "black",
                                    "backgroundColor": "white",
                                },
                            ),
                        ]
                    ),
                    width=3,
                    style={"padding": "0 10px"},
                ),
            ],
            align="center",
            style={"margin": "0"},
        )
    ]
)

output = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(
                    html.Div(
                        [
                            dbc.Row(
                                html.Div(
                                    [
                                        dbc.Card(
                                            dbc.CardBody(
                                                [
                                                    html.H4(
                                                        "Success Rate",
                                                        className="card-title",
                                                    ),
                                                    html.P(
                                                        id="success-rate-value",
                                                        className="card-text",
                                                        style={"fontSize": "24px"},
                                                    ),
                                                ]
                                            ),
                                            style={
                                                "flex": "1",
                                                "marginBottom": "10px",
                                                "width": "100%",
                                            },
                                        ),
                                        dbc.Card(
                                            dbc.CardBody(
                                                [
                                                    html.H4(
                                                        "Fee",
                                                        className="card-title",
                                                    ),
                                                    html.P(
                                                        id="fee-value",
                                                        className="card-text",
                                                        style={"fontSize": "24px"},
                                                    ),
                                                ]
                                            ),
                                            style={
                                                "flex": "1",
                                                "marginBottom": "10px",
                                                "width": "100%",
                                            },
                                        ),
                                        dbc.Card(
                                            dbc.CardBody(
                                                [
                                                    html.H4(
                                                        "Admitted",
                                                        className="card-title",
                                                    ),
                                                    html.P(
                                                        id="admitted-value",
                                                        className="card-text",
                                                        style={"fontSize": "24px"},
                                                    ),
                                                ]
                                            ),
                                            style={
                                                "flex": "1",
                                                "marginBottom": "10px",
                                                "width": "100%",
                                            },
                                        ),
                                    ],
                                    style={
                                        "display": "flex",
                                        "flexDirection": "row",
                                        "gap": "10px",
                                        "justifyContent": "center",  # Centering cards horizontally
                                    },
                                ),
                                style={
                                    "padding": "0 10px",
                                    "justifyContent": "center",  # Centering the row
                                },
                            ),
                            dbc.Col(
                                [
                                    dbc.Row(
                                        html.Div([dcc.Graph(id="map-graph")]),
                                        style={
                                            "paddingLeft": "0 20px",
                                            "width": "100%",
                                            "flex": "1",
                                            "margin": "0 auto",
                                        },
                                    ),
                                    dbc.Row(
                                        html.Div(
                                            [dcc.Graph(id="university-bar-chart")]
                                        ),
                                        style={
                                            "paddingRight": "0 20px",
                                            "width": "100%",
                                            "flex": "1",
                                            "margin": "0 auto",
                                        },
                                    ),
                                ],
                                style={
                                    "gap": "2",
                                    "display": "flex",
                                    "width": "100%",
                                    "margin": "0 auto",
                                },
                            ),
                        ],
                        style={
                            "textAlign": "center",  # Center text if needed
                        },
                    ),
                    width=12,  # Full width column for centering
                ),
            ],
            style={"padding": "20px 0", "margin": "0 auto"},
        )
    ]
)


# Define the additional output section with more charts and a data table
additional_output = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(
                    html.Div([dcc.Graph(id="major-pie-chart")]),
                    width=4,  # Width of the first column
                    style={
                        "padding": "0 10px"
                    },  # Add padding to prevent content from being too close to the edges
                ),
                dbc.Col(
                    html.Div([dcc.Graph(id="university-line-chart")]),
                    width=4,  # Width of the second column
                    style={
                        "padding": "0 10px"
                    },  # Add padding to prevent content from being too close to the edges
                ),
                dbc.Col(
                    html.Div(
                        [
                            dash_table.DataTable(
                                id="data-table",
                                columns=[
                                    {"name": col, "id": col} for col in df.columns
                                ],
                                style_table={"overflowX": "auto"},
                                style_cell={"textAlign": "left"},
                                page_size=10,
                            )
                        ]
                    ),
                    width=4,  # Width of the third column
                    style={
                        "padding": "0 10px"
                    },  # Add padding to prevent content from being too close to the edges
                ),
            ],
            style={
                "padding": "20px 0",
                "color": "black",
                "margin": "0 auto",
            },  # Add padding to the row
        )
    ]
)

# Define the app layout to include the navbar, header, filters, and output sections
app.layout = html.Div(
    children=[
        navbar,
        header,
        filter,
        output,
        additional_output,  # Add the new output section to the layout
    ]
)


# Callback to update the visualizations based on filter and sort inputs
@callback(
    [
        Output("university-bar-chart", "figure"),
        Output("map-graph", "figure"),
        Output("success-rate-value", "children"),
        Output("fee-value", "children"),
        Output("admitted-value", "children"),
        Output("major-pie-chart", "figure"),
        Output("university-line-chart", "figure"),
        Output("data-table", "data"),
    ],
    [
        Input("university-dropdown", "value"),
        Input("major-dropdown", "value"),
        Input("course-dropdown", "value"),
    ],
)
def update_visualizations(selected_university, selected_major, selected_course):
    # Handle "Select All" option for universitys
    if "all" in selected_university:
        selected_university = df["uni"].unique().tolist()

    # Filter data based on selected universitys
    filtered_df = df[df["uni"].isin(selected_university)]

    # Handle "All" option for major
    if selected_major == "all":
        # Compute total counts for both majors
        average_success_rate = filtered_df["success_rate"].sum() / len(
            filtered_df["success_rate"]
        )
        average_fee = filtered_df["fee"].sum() / len(filtered_df["fee"])
        filtered_df["total_admitted"] = filtered_df[
            ["round1", "round2", "round3", "round4"]
        ].sum(axis=1)
        total_admitted = filtered_df["total_admitted"].sum()
        y_values = "major"
    else:
        filtered_df = df[df["major"].isin([selected_major])]
        average_success_rate = filtered_df["success_rate"].sum() / len(
            filtered_df["success_rate"]
        )
        average_fee = filtered_df["fee"].sum() / len(filtered_df["fee"])
        filtered_df["total_admitted"] = filtered_df[
            ["round1", "round2", "round3", "round4"]
        ].sum(axis=1)
        total_admitted = filtered_df["total_admitted"].sum()
        y_values = selected_major

    if selected_course == "all":
        # Compute total counts for both majors
        average_success_rate = filtered_df["success_rate"].sum() / len(
            filtered_df["success_rate"]
        )
        average_fee = filtered_df["fee"].sum() / len(filtered_df["fee"])
        filtered_df["total_admitted"] = filtered_df[
            ["round1", "round2", "round3", "round4"]
        ].sum(axis=1)
        total_admitted = filtered_df["total_admitted"].sum()
        y_values = "course"
    else:
        filtered_df = df[df["course"].isin([selected_course])]
        average_success_rate = filtered_df["success_rate"].sum() / len(
            filtered_df["success_rate"]
        )
        average_fee = filtered_df["fee"].sum() / len(filtered_df["fee"])
        filtered_df["total_admitted"] = filtered_df[
            ["round1", "round2", "round3", "round4"]
        ].sum(axis=1)
        total_admitted = filtered_df["total_admitted"].sum()
        y_values = selected_course

    sorted_df = filtered_df

    # Create Bar Chart
    bar_fig = px.bar(
        sorted_df,
        x="uni",
        y=["total_admitted"] if selected_major == "all" else y_values,
        title="Number of Admiited in 2566",
        labels={
            "uni": "University",
            "value": "Number of Admiited",
        },
        barmode="relative",
    )

    # Create Pie Chart
    success_data = {
        "label": ["Success", "Fail"],
        "value": [average_success_rate, 100 - average_success_rate],
    }
    success_rate = pd.DataFrame(success_data)
    pie_fig = px.pie(
        success_rate,
        names="label",
        values="value",
        title="Success Rate Distribution of Graduates in 2566",
    )

    # Create Line Chart
    line_fig = px.line(
        filtered_df,
        x="uni",
        y=["total_admitted"],
        title="Trend of Admiited in 2566",
        labels={
            "uni": "University",
            "value": "Number of Admiited",
        },
    )

    # Create Data Table
    table_data = filtered_df.to_dict("records")

    if not selected_university:
        lat, lon, zoom = df['lat'].mean(), df['lon'].mean(), 5
    else:
        last_clicked_university = selected_university[-1]
        lat = df[df["uni"] == last_clicked_university]["lat"].values[0]
        lon = df[df["uni"] == last_clicked_university]["lon"].values[0]
        zoom = 15

    map_fig = px.scatter_mapbox(
        df,
        lat="lat",
        lon="lon",
        hover_name="uni",
        zoom=zoom,
        height=450,
    )
    map_fig.update_layout(mapbox=dict(center=dict(lat=lat, lon=lon)))

    map_fig.update_traces(marker=dict(size=10, color='rgba(0, 0, 255, 0.5)', opacity=0.7), selector=dict(mode='markers'))
    for university in selected_university:
        map_fig.add_trace(
            go.Scattermapbox(
                lat=[df[df["uni"] == university]["lat"].values[0]],
                lon=[df[df["uni"] == university]["lon"].values[0]],
                mode="markers",
                marker=go.scattermapbox.Marker(size=20, color="red", opacity=0.9),
                name=university,
            )
        )
    map_fig.update_layout(mapbox_style="open-street-map")
    map_fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

    return (
        bar_fig,
        map_fig,
        average_success_rate,
        average_fee,
        total_admitted,
        pie_fig,
        line_fig,
        table_data,
    )


# Run the app
if __name__ == "__main__":
    app.run(debug=True, port=8080)
