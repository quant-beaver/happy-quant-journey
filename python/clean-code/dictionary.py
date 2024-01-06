numberOfPets = {'dogs': 5}
numberOfPets.setdefault('cats', 0)

# bad
if 'cats' in numberOfPets:
    print("cats check")
else:
    print("zero cats")
    
# good
print ("I have cats", numberOfPets.get('cats', 0))
print ("I have dogs", numberOfPets.get('dogs', 0))
