# 디폴트 파라미터와 키워드 파라미터에 대한 데모 (**아주 중요)

def cube(number=1):
    return number ** 3


def add_two_number(one=0, two=0):
    return one + two


def main():
    print(add_two_number(0, 4))
    print(add_two_number(two=4))
    # print(cube())


main()
