# As fast as possible - 1hr TUT

# Data Types
# Int
int_a = -267236
int_b = 76373

# Float
c = 2727.0
d = -9.3
# String
greet_A = 'Hello'
greet_B = "World"

# Bool
bool_x = True
bool_y = False

# printing 2 Console
print("Hello World!")
print(4.5, "Hello", 'end', 87, False, end='\n') # Move to next line
print("Next Line")

hello = "Matthew"
world = "World"
print(hello, world)

# Naming - snakecase
# eg - hello_world
# 9hello # don't start with numbers

#user input
input("Enter your name: ")
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
age = input("Enter your age: ")
# Concat
print("Hello", first_name, last_name, "Your are:", age, "Years old")

# Arithmetic Operators
x = 9
y = 3
result = x + y
print(result)
result = x - y
print(result)
result = x / y
print(result)
result = int(x * y)
print(result)
# exponent
result = x ** y
print(result)
result = x // y
print(result)
result = x % y
print(result)

base = 2
exponent = 3
result = base ** exponent
print(result)  # Output: 8

x = 3
y = 2
result = x ** y
print(result)  # Output: 9

# Convert data types
num = input('Number: ') # -> str
print(int(num) - 5)
num = input('Number: ') # -> str
print(float(num) - 5)

# String Methods
hello = 'hello'
print(type(hello)) # Output: str
hello_A = 'hello'.upper() # Output: HELLO
hello_B = 'Hello'
print(hello_B.lower()) # Output: hello
hello_C = "HellO WorlD"
print(hello_C.capitalize())
hello_C = "HellO WorlD"
print(hello_C.count('l')) # -> count the l's in lower case

x_a = "hello"
y_a = 3
print(x_a * y_a) # -> hellohellohello

x_b = "hello"
y_b = "world"
print(x_b * y_b) # -> helloworld

# Conditinal Operators
# == | != | <= | >= < | >

x = "hello"
y = "hello"
print(x == y) # True
print(x != y) # False

print('a' > 'z') # True
print(ord('a')) # 97
print(ord('z')) # 90
print(7.5 > 7)

result = 6 == 6
print(result)

# Chained Conditionals

x = 7
y = 8
z = 0
result_1 = x == y
result_2 = y > x
result_3 = z < x + 2

# not | and | or -> in order

result_4 = result_1 or result_2
result_4 = result_1 or not result_2
result_4 = result_1 and result_2

# IF | ELSE | ELIF

# IF
x = input('Name: ')

if x == "Matt":
    print("You are good at PY!!!")
    print()

print("Allways do this")

# IF | ELSE
x = input('Name: ')

if x == "Matt":
    print("You are good at PY!!!")
else:
    print("You suck!!!")

# IF | ELSE | ELIF

x = input('Name: ')

if x == "Matt":
    print("You are good at PY!!!")
elif x == "John":
    print("Hello John")
else:
    print("You suck!!!")

# list & Tuples
# list ordered collection
x = [4, True, 'A', "Hello"]
print(x)
print(len(x))
x.append("World")
x.extend([4, 5, 6, 7, 8, 9])
print(x)
print(x.pop())
print(x.pop(0))
# Tuples - immutable
x_Tuple = (0, 0, 2, 2)
print(x_Tuple)
y_tuple = x_Tuple + (3, 3, 4, 4)
print(y_tuple)

# Loops
# for loops
for i in range(10): # -> start, stop, step
    print(i)

for i in range(1, 100, 2): # -> odd numbers
    print(i)

for i in range(2, 23,2): # -> even numbers
    print(i)

for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]: # -> loop thru a list
    print(i)

x = [3, 4, 42, 3, 2, 4]
for i in range(len(x)):
    print(x[i])

for i, element in enumerate(x):
    print(i, element)

# While loops
i = 0
while i < 10:
    print('run')
    i += 1

i = 0
while True:
    print('run')
    i += 1
    if i == 10:
        break

# Slice Operator - lists
x = [0, 1, 2, 3, 4, 5, 6, 7, 8]
y = ['hi', 'hello', 'goodbye', 'cya', 'sure']
s = "Hello"

sliced = x[0:5:2] # -> start:stop:step
sliced_a = x[::-1] # -> reverse the list
sliced_b = x[::2] # -> step the list by 2

print(sliced)
print(sliced_a)

# Slice Operator - tuples
sliced_c = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)[::-1]
print(sliced_c)

# Sets data type - unordered - fast for lookups - see if something exists or not
x = set() # -> empty set
set_a = {4, 32, 2, 2}
print(set_a)
set_a.add(5)
print(set_a)
set_a.remove(5)
print(set_a)
print(4 in set_a)
print(33 in set_a)
set_b = {3, 4, 22, 1}
print(set_a.union(set_b))
print(set_a.difference(set_b))
print(set_a.intersection(set_b))

# Dictionaries -> key : value pair
dic_x = {'key': 4}
print(dic_x['key'])
dic_x['key2'] = 5
dic_x[2] = 8
print(dic_x)
print('key' in dic_x)
print(dic_x.values())
print(dic_x.keys())
del dic_x['key']
for key, value in dic_x.items():
    print(key, value)

for key in dic_x:
    print(key, dic_x[key])

# Comprehensions
x = [x for x in range(5)]
print(x)

x = [x % 5 for x in range(5)]
print(x)

x = [[0 for x in range(100)] for x in range(5)]
print(x)

x = [i for i in range(100) if i % 5 == 0]
print(x)

x = {i for i in range(100) if i % 5 == 0} # -> Dic version
print(x)

x = tuple(i for i in range(100) if i % 5 == 0) # -> tuple version
print(x)

# Functions -> use of def keyword

def func():
    print("run")

func()

def func():
    print("run")
    def func():
        print('hi')
    func()

func()

# Functions -> args

def func(x, y):
    print("run", x, y)

print(5, 6)
def func(x, y):
    print("run", x, y)
    return x * y

print(func(5, 6))

def func(x, y):
    print("run", x, y)
    return x * y, x / y

print(func(5, 6))

def func(x, y):
    print("run", x, y)
    return x * y, x / y

r1, r2 = func(5, 6)
print(r1, r2)

def func(x, y, z=None):
    print("run", x, y, z)
    return x * y, x / y

r1, r2 = func(5, 6, 7)
print(r1, r2)

# Unpack operator / ARGS & KWARGS

def fun(x):
    def func_2():
        print(x)
    return func_2

print(func(3)())

def func(*args, **kwargs):
    pass

x = [1, 23, 2367, 2727]
print(x)
print(*x)

def func(x, y):
    print(x, y)

pairs = [(1, 2), (3, 4)]

for pairs in pairs:
    func(*pairs)

def func(x, y):
    print(x, y)

    func(**{"y": 2, "x": 5})

def func(*args, **kwargs):
    print(args, kwargs)

func(1,2,3,4,5,one=0, two=1)

# Scope and Global

name_x = "tim" # -> Global

def func(name):
    name_x = name # -> Local

print(name_x)
func('changed')
print(name_x)
###
name_m = "matt" # -> Global

def func(name):
    global name_m # -> Local
    name_m = name

print(name_m)
func('changed')
print(name_m)

# Exceptions

raise Exception('Bad')

# Handling Exceptions -> try except finally

try:
    x = 7 / 0
except Exception as e:
    print(e)
finally:
    print("finally")

# lamdba

x = lambda x: x + 5
print(x(2))

# Map & filter

x = [1, 2, 3,4,5,6,7,313,23,142,4]

mp = map(lambda i: i + 2, x)
print(list(mp))

mp = filter(lambda i: i % 2 == 0, x)
print(list(mp))

# F Strings

tim = 89
x = f'hello {6 + 8} {tim} {69 + 9}'
print(x)
print(f'hello {tim}')
