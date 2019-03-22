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
```

```python
# TUPLES
# are immutable : you cannot change them, delete from/update. Only access
# you can combine 2 tuples together: tup3 = tup1 + tup2
# del tup, len tup, tup + 4
tup = ('tulips','roses')
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
