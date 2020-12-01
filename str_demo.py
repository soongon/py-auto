# 스트링 사용법 데모
my_str = 'Hello World!'

# 1. 스트링의 문자 추출 by Index(0 based int index)
# W 를 추출
print(my_str[6])
# d 를 추출 (마이너스 인덱스를 사용, -1부터 시작하고 뒤에서 카운팅)
print(my_str[-2])

# 2. 스트링 자르기(Slicing)
print(my_str[1:5])  # ello
print(my_str[-6:-2])  # Worl
print(my_str[:5])  # Hello
print(my_str[6:])  # World!

# 3. 슬라이싱 사례
# *Hello World* 글자에서 * 제거하고 문자만 추출하기
problem_01 = '*Hello World*'

print(problem_01[1:-1])

