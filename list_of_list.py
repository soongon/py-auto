# list of list --> 이중 리스트, 이차원 행렬, 표형 데이터, 열과 행이 존재
# 4층 짜리 아파트의 각 집을 표현
apart = [
    [401, 402, 403, 404],
    [301, 302, 303, 304],
    [201, 202, 203, 304],
    [101, 102, 103, 104]
]

print(apart[1][1])
print(apart[3][3])

for row in apart:
    for home in row:
        print(home)
