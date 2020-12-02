import pickle

favorite_colors = ['red', 'black', 'white']

with open('color.pickle', 'wb') as file:
    pickle.dump(favorite_colors, file)

print('file saved with pickle..')

with open('color.pickle', 'rb') as file:
    colors = pickle.load(file)

print(type(colors))
print(colors)
