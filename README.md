# Python-Udemy-Tutorial

### All the basics

```python
# MULTIPLE ASSIGNMENT
diana, alex, dana = 20, 17, 21
diana = alex = dana = 20
name, age = 'Dana', 20
```

```python
"Hi" * 3
"HiHiHi"

std = "Dana is a student"
std[0:4]

"Dana"
std[-2]
"n"

std[0:-3]
"Dana is a stud"
```

```python
name = "Jake"
msg = "%s is 17 years old"
msg%name
"Jake is 17 years old"
msg%("Alex")
"Alex is 17 years old"
msg = "%s %d is cool"
msg("Jake",100)
"Jake 100 is cool"
```

```python
# LISTS
shopList = ['Apples','Oranges','Cheese']

del shoplist[1]

len(shopList)
3

shopList2 = ['Avocado']
shopList + shopList2
['Apples','Oranges','Cheese','Avocado']
numberList = [1,2,3]

max(numberList)
3
min(numberList)
1

# One list can have different types inside: lst = [20,4,'Bernard',10.3]
list.append(2)
list.remove(2)
list.insert(3,99)
list.sort(reverse = True)

[Difference between append and extend](https://stackoverflow.com/questions/252703/difference-between-append-vs-extend-list-methods-in-python)
```

```python
# DICTIONARIES
students = {'Bob':12, 'Anne':13, 'Sara':15}
students['Bob']
12

del student['Sara']

# !!! we shouldn't have dictionaries like this
dont = {'Bob':1,'Bob':2,'Bob':3}
students['Bob']
3

dict.items()
dict.keys()
dict.values()

```

```python
# TUPLES
# are immutable : you cannot change them, delete from/update. Only access
# you can combine 2 tuples together: tup3 = tup1 + tup2
# del tup, len tup, tup + 4
tup = ('tulips','roses')
tpl = (30,)
# if I want to define a tuple with only one element, I should use the comma after it so that it recognizes it as a tuple and not as a number
tpl.index(30)
tuple(list)
```

```python
if ( 1 < 10):
	print("true")
elif ( 5 > 4 and 2 > 7):
	print("elif")
else:
	print("false")
# You need if and else to be on the same line, and the rest has to be on the next tab

```

```python
# FOR
list = ['A','B','C']
for item in list:
	print(item)
# you can also iterate through tuples

for i in range(1, 11):
	print(i)
# prints numbers 1-10

for i in range(0,10,2):
	print(i)
# skips numbers like i=i+2 => 0 2 4 6 8
```

```python
# WHILE, break, continue
c = 0
while c < 5:
	c = c + 1
	if c == 3:
		continue
	print(c)
# prints 1 2 4 5

c = 0
while c < 5:
	c = c + 1
	if c == 3:
		pass
	print(c)
# pass doesn't do anything, lets you put some filler code until you know what code you re gonna put there
# prints 1 2 3 4 5
```

```python
# TRY EXCEPT
try:
	if(name > 3)
		print("You have defined your variable name")
except:
	print("There's something wrong with your code")
```

```python
# COMMENTS
# this is a comment
"""
this is
a multi-line comment 
yay
"""
```

```python
# FUNCTIONS
def SayHi(name):
    print("Hi " + name + "! <3")

SayHi("Alex")
```

```python
# IN-BUILT FUNCTIONS
abs(-23) => 23

bool(0) => False
bool(None) => False
bool(100) => True - anything besides 0

dir("Hello") => gives me list of all the functions i could use with that parameter

help(nume.upper) => explains what the function do 

sent = 'print("Hi")'
eval(sent)
Hi 

eval(5*3)
15

a = 1
str(a) => '1'
float(a) => 1.0
int(a) => 1

```

### Python Core and Advanced Course

```python
a = 25.0
print(typeof(a))
# COMPLEX TYPES
d = 4 + 5j
# BINARY TYPES
b = 0B1010
print(b) => prints 10
# HEXADECIMAL TYPES
c = 0XFF
print(c) => prints 255
# BOOLEAN TYPES
e = True
```

```python
# MORE ABOUT STRINGS
sir = """You
are
awesome"""
s[2:] => starts from index 2, goes all the way to the end
s[:5] => start from the very beginning, go up to index 8
s[::-1] => start from the end, get REVERSE STRING
s.strip() => remove spaces at the beginning and at the end of string s
s.lstrip()
s.rstrip()
s.find("string",startIndex,endIndex)
s.count('a')
s.replace("awesome","super")
s.upper, lower, title() => You Are Awesome
```

```python
# SETS
s = {10,20,'XYZ'}
s.update([30,25])
s.remove(30)
# does not guarantee order
# set object does not support indexing
# is not subscriptable - does not allow slicing
# does not allow repetition ( s*3 )
f = frozenset(s)
# does not allow update/remove
```

```python
a**b  => a to the power of b
a//b => returns integer always, while a/b returns float
we also have **= and //=
```

```python
#INPUT/OUTPUT FUNCTIONS
a,b= 10, 20
print(a,b,sep=',') => 10,20
name = 'Dana'
mark = 10.5
print('name is ', name)
print("name is %s, mark is %f"%(name,mark)) => name is Dana, mark is 10.500000
print("name is %s, mark is %2.f"%(name,mark)) => name is Dana, mark is 10.50
print("name is {}, mark is {}".format(name, mark))
print("name is {0}, mark is {1}".format(name, mark))

s = input("Enter your name: ")
i = int(input("Enter your number: "))

lst = [x for x in input("Enter 3 numbers separated by space: ").split()] => write 1 2 3, you get ['1','2','3']
lst = [x for x in input("Enter 3 numbers separated by comma: ").split(',')] => write 1,2,3, you get ['1','2','3']
lst = [int(x) for x in input("Enter 3 numbers separated by space: ").split()] => => write 1 2 3, you get [1,2,3]
```

```python
import math
math.pi
```

```python
x = (int(input("Enter a number greater than 10"))
assert x>10, "Wrong number"
print("you entered ",x)
```

```python
import sys

list = sys.argv
for i in list: print(i,' ')
```

```python
Functions can return multiple values!!!
def f(a,b):
	return a+b, a-b
result = f(2,3)
print(type(result)) => tuple
```

```python
x = 1
def display():
	x = 2
	print(x)
	print(globals['x'])
f = display
f()
f()
```

```python
def display():
	def message():
		return "hi"
	return message

fun = display()
print(fun()) => hi
```

```python
# keyword arguments
def display(a,b)
	print(a,',',b)

display(10,20) => 10,20
display(b=10, a=20) => 20,10

# default arguments
# we can do this too:
def display(a = 10,b = 20)
	print(a,',',b)
display(a=30) => 30,20  #sweet
```

```python
# LAMBDA FUNCTIONS
instead of:
def cube(x)
	return x**3
# just write: 
f = lambda x:x**3
print(f(2))
# will always return a function back
# rarely using them like this. they are very useful when we use them inside other functions
l = lambda x : 'EVEN' if x%2 == 0 else 'ODD'
l = lambda a,b: a+b

lst = [1,2,3,4,5]
result = list(filter(lambda x:x%2==0,lst))

lst = [2,3,4,5]
result = list(map(lambda n:n*2, lst))
print(result) => [4,6,8,10]

lst = [5,10,15,20]
result = reduce(lambda x,y:x+y, lst)
print(result) => 50
```

```python
# A decorator takes a function and it will return a function but the function that is returned by
# the decorator will perform additional logic or additional processing on the function that is given as input.
def decor(fun):
	def inner():
		result = fun()
		return result*2
	return inner

def num():
	return 5

resultfun = decor(num)
print(resultfun()) => 10

# METHOD 2. after writing def decorfun(fun): ...

@decorfun
def num():
	return 5
	
print(num())

# Another example:
def decorfun(fun):
	def inner(n):
		result = fun(n)
		result += " How are you?"
		return result
	return inner

@decorfun
def hello(name)
	return "Hello " + name
	
print(hello("Dana")) => Hello Dana How are you?
```

```python
# GENERATORS
# Generators are functions that return a sequence of values back
# A generator function is returned just like any other function but it uses a yield statement

def customgen(x,y):
	while x<y
		yield x
		x+=1
		
result = customgen(20,30)
for i in result: print(i) => 20 21 ... 29
```

```python
import mymath as ma

print(ma.sum(19,4))

# METHOD 2

from mymath import*
print(sum(2,2))
```

```python
# LIST EXTRAS
# instead of:
lst=[]
for x in range (1,11)
	lst.append(x**3)
print(lst)

lst=[]
lst = x**3 for x in range(1,11)

-------------------------------------

lst = [x for x in range(1,21) if x%2==0]

a=[1,2,3]
b=[3,45,5]
z = []
z =[a[i]*b[i] for i in range(len(a))]

commonElements = [i for i in a if i in b]
```

```python
# STATIC METHODS
class ObjCounter:
	nrOfObj = 0
	
	def __init__(self):
		ObjectCounter.nrOfObj += 1

	@staticmethod
	def displayCount():
		print(ObjCounter.nrOfObj)

o1 = ObjCounter()
o2 = ObjCounter()

ObjCounter.displayCount() => 2
```

```python
self.__id=123 => makes it PRIVATE
print(s._Student__id)
# name mangling
```

