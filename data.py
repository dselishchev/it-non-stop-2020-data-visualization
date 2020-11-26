import os

import pandas as pd

base_dir = os.path.dirname(os.path.abspath(__file__))
df_csv_path = os.path.join(base_dir, '2020_june_mini.csv')

df: pd.DataFrame = pd.read_csv(df_csv_path)