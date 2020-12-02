file = open('./data/zen_of_python.txt')

print(type(file))
print(file)

# line = file.readline()
# print(line)

lines = file.readlines()

print(lines)

file.close()
