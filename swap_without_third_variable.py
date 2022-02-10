x = int(input('Enter value of x: '))
y = int(input('Enter value of y: '))

# create a temporary variable and swap the values
#x, y = y, x
#Adding
x = x + y
y = x - y
x = x - y

print('The value of x after swapping: {}'.format(x))
print('The value of y after swapping: {}'.format(y))