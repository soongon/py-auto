# 스트링 여러 메소드 데모

my_str = 'Python is a very interesting programming language.'

print(len(my_str))

# split
splitted = my_str.split(' ')

print(type(splitted))
print(splitted)

# join
joined = ' '.join(splitted)
print(type(joined))
print(joined)

# in, not in
is_member = 'Python' not in my_str
print(type(is_member))
print(is_member)

if 'Python' in my_str:
    print('It is true')
else:
    print('It is not true')

# upper(), lower(), isupper(), islower(), startswith(), endswith()
print('Python'.upper())
print('Python'.lower())
print('Python'.startswith('Pyth'))
print('Python'.endswith('hon'))