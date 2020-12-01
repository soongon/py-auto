# 리스트 데모
favorite_colors = ['red', 'blue', 'purple', 'brown', 'pink', 'white']

# CRUD
favorite_colors.append('검정')
print(favorite_colors)

favorite_colors.insert(2, '보라빛향기')
print(favorite_colors)

print(favorite_colors[-2])
print(favorite_colors[2:5])

del favorite_colors[2]
print(favorite_colors)

favorite_colors.remove('purple')
print(favorite_colors)
