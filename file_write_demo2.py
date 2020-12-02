file_contents = [
    'hello world\n',
    '안녕하세요\n',
    '반가워요, 니하오\n'
]

with open('./data/my-file2.txt', 'w') as file:
    file.writelines(file_contents)

print('job completed..')
