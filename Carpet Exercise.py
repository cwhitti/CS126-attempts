# Main function

    # Show + followed by 10 /\ followed by +
print('+', end = '')
for index in range (10):# <- Loop!!!
    print('/\\', end = '')
print('+')

    # Show | followed by 20 spaces and then |. Repeat 5 times alltogether
for index in range(5):
    print('|', end = '')
    print(' ' * 20, end = '')
    print('|')
    
    # Show + followed by 10 /\ followed by +
print('+', end = '')
for index in range (10):# <- Loop!!!
    print('/\\', end = '')
print('+', end = '')

    # show 2 blank lines
print('\n'*2,)

    # Show + followed by 4 /\ followed by +
print('+', end = '')
for index in range (4):# <- Loop!!!
    print('/\\', end = '')
print('+')

    # Show | followed by 8 spaces and then |. Repeat 2 times alltogether
for index in range(2):
    print('|', end = '')
    print(' ' * 8, end = '')
    print('|')

    # Show + followed by 4 /\ followed by +
print('+', end = '')
for index in range (4):# <- Loop!!!
    print('/\\', end = '')
print('+')


----- oops
# Constants
x = 8
y = x*2


# Top part of carpet
def top():
    print('+', end = '')
    for index in range (x):
        print('/\\', end = '')
    print('+')
# middle carpet
def middle():
    print('|', end = '')
    for index in range (y):
        print(' ', end = '')
    print('|')

top()
middle()
top()


