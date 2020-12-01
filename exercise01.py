# 연습문제. 입력받은 문자의 첫글자를 마지막으로 옮기고 ay 를 추가하여 출력

input_from_user = input('글자를 입력하고 엔터키를 치세요..\n')

if len(input_from_user) > 0 and input_from_user.isalpha():
    # soongon --> oongons
    converted = input_from_user[1:] + input_from_user[0] + 'ay'
    print(converted)
else:
    print('최소 한글자 이상 문자만 입력해 주세요.')

#  https://github.com/soongon/py-auto