# 딕셔너리 데모
directors = {
    '봉준호': '기생충',
    '강우석': '투캅스',
    'cameron': 'titanic',
    '박찬욱': '아가씨'
}

# CRUD
print(directors['봉준호'])
directors['김기덕'] = '봄여름가을겨울..'
print(directors)
del directors['김기덕']
print(directors)

# print(directors['박찬우'])
print(directors.get('박찬우'))

if directors.get('박찬우'):
    print(directors.get('박찬욱'))
else:
    print('데이터가 없습니다.')