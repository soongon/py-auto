import pandas as pd

df = pd.read_csv('./data/top_films.csv', index_col='Rank')

print(type(df))
print(df)

print(df.info())

df['Admissions(millions)'] = df['Admissions(millions)'] * 1_000_000

print(df)

df.to_csv('./data/top_films_pandas_converted.csv')
print('job completed..')
