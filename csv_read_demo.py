import csv
import pprint

with open('./data/top_films.csv') as file:
    reader = csv.reader(file)
    film_list = list(reader)

# 관객의 수를 백만을 곱해서 숫자로 변경
for i, row in enumerate(film_list):
    if i == 0:
        continue  # 첫번째 줄은 패스
    for j, item in enumerate(row):
        if j == 1:
            film_list[i][j] = float(item) * 1_000_000

pprint.pprint(film_list)

# 이중 리스트를 저장
with open('./data/top_films_converted.csv', 'w', newline='') as file:
    output_writer = csv.writer(file)

    for row in film_list:
        output_writer.writerow(row)

print('job completed..')
