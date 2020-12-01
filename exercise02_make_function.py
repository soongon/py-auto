# 함수만들기 연습

def cube(number):
    return number ** 3


def by_three(number):
    if number % 3 == 0:
        return cube(number)
    else:
        return False


print(cube(5))
print(by_three(9))
