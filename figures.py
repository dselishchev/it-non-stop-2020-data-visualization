__all__ = [
    'city_salaries_figure',
    'position_salaries_figure',
    'se_positions_pie_chart',
]

import pandas as pd
from plotly.express import bar, pie, scatter

from data import df

se_df = df[df['Должность'].str.lower().str.contains('software engineer')]
qa_df = df[df['Должность'].str.lower().str.contains('qa engineer')]

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
