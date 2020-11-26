import dash_core_components as dcc
import dash_html_components as html

from figures import (
    cities_positions_bubble_chart,
    city_salaries_figure,
    position_salaries_figure,
    qa_positions_pie_chart,
    se_positions_pie_chart,
)


def get_layout():
    return html.Div(
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
