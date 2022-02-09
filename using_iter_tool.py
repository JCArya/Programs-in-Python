import itertools

list_1 = [1, 2, 3, 4, 5, 6]
list_2 = ['a', 'b', 'c']

# loop until the short loop stops
for i,j in zip(list_1,list_2):
    print(i,j)

print("\n")

# loop until the longer list stops
for i,j in itertools.zip_longest(list_1,list_2):
    print(i,j)