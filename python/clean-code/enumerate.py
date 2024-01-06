# bad
animals = ['cat', 'dog']
for i in range(len(animals):
    print(i, animals[i])

# good
animals = ['cat', 'dog', 'dodo']
for i, animals in enumerate(animals):
    print(i, animals)
    
# without index
animals = ['cat', 'dog', 'dodo']
for animal in animals:
    print(animal)