import os

import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
from plotly.express import bar, pie, scatter

# Load DataFrame
base_dir = os.path.dirname(os.path.abspath(__file__))
df_csv_path = os.path.join(base_dir, '2020_june_mini.csv')

df: pd.DataFrame = pd.read_csv(df_csv_path)

# Filter DataFrame for QA and SE
se_df = df[df['Должность'].str.lower().str.contains('software engineer')]
qa_df = df[df['Должность'].str.lower().str.contains('qa engineer')]

# Create charts
cities_grouped_df: pd.DataFrame = df.groupby('Город').median()
city_salaries_figure = bar(cities_grouped_df, x=cities_grouped_df.index,
                           y='Зарплата.в.месяц')
position_grouped_df: pd.DataFrame = df.groupby('Должность').median()
position_grouped_df = position_grouped_df.sort_values(['Зарплата.в.месяц'])
position_salaries_figure = bar(position_grouped_df, x=position_grouped_df.index, y='Зарплата.в.месяц')

se_positions_pie_chart = pie(se_df, names=se_df['Должность'])
qa_positions_pie_chart = pie(qa_df, names=qa_df['Должность'])

cities_positions_grouped: pd.DataFrame = df.groupby(['Город', 'Должность']).median()
cities_positions_bubble_chart = scatter(cities_positions_grouped, x=[i[0] for i in cities_positions_grouped.index],
                                        y=[i[1] for i in cities_positions_grouped.index], size='Зарплата.в.месяц',
                                        size_max=45)

# Create layout
layout = html.Div(
    className='row',
    children=[
        # Bar Charts
        html.Section(
            children=[
                html.Div(
                    children=[html.H1('Медианная зарплата по городам')]
                ),
                html.Div(
                    children=[
                        dcc.Graph(
                            figure=city_salaries_figure,
                        )
                    ]
                ),
            ],
        ),
        html.Section(
            children=[
                html.Div(
                    children=[html.H1('Медианная зарплата по специализациям')]
                ),
                html.Div(
                    children=[
                        dcc.Graph(
                            figure=position_salaries_figure,
                        )
                    ]
                ),
            ],
        ),
        # Pie Charts
        html.Section(
            children=[
                html.Div(
                    className='row',
                    children=[
                        html.Div(
                            className='six columns',
                            children=[
                                html.Div(
                                    children=[html.H1('Распределение Software Engineer')]
                                ),
                                html.Div(
                                    children=[
                                        dcc.Graph(
                                            figure=se_positions_pie_chart,
                                        )
                                    ]
                                ),
                            ]
                        ),
                        html.Div(
                            className='six columns',
                            children=[
                                html.Div(
                                    children=[html.H1('Распределение QA Engineer')]
                                ),
                                html.Div(
                                    children=[
                                        dcc.Graph(
                                            figure=qa_positions_pie_chart,
                                        )
                                    ]
                                ),
                            ]
                        ),
                    ]
                ),

            ],
        ),
        # Bubble Charts
        html.Section(
            children=[
                html.Div(
                    className='row',
                    children=[
                        html.H1('Зарплаты по городам и должностям'),
                        dcc.Graph(figure=cities_positions_bubble_chart,
                                  style={'height': '1000px'}),
                    ]
                )
            ]
        ),
    ],
)

dash_app = dash.Dash('My Awesome Data Visualization App')
dash_app.title = 'My Awesome Data Visualization App'
dash_app.layout = layout

app = dash_app.server
