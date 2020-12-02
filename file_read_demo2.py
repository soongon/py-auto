
try:
    with open('./data/zen_of_pytho.txt') as file:
        for line in file:
            print(line, end='')
except:
    print('파일이 없습니다. 작업이 정상적으로 수행되지 않았습니다.')

print('job completed..')
