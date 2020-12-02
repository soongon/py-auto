# 스티븐 스필버그(Steven Spielberg) 감독 작품 필터링
import pandas as pd

df = pd.read_csv('./data/top_films.csv', index_col='Rank')

filtered_df = df.loc[df['Director(s)'] == 'Steven Spielberg']

filtered_df.to_csv('./data/top_films_ss_filtered.csv')

print('job completed..')
