# Python-Udemy-Tutorial

### All the basics

```
# MULTIPLE ASSIGNMENT
diana, alex, dana = 20, 17, 21
diana = alex = dana = 20
name, age = 'Dana', 20
```

```
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

```
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

```
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

```
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

```
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

```
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

```
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

```
# TRY EXCEPT
try:
	if(name > 3)
		print("You have defined your variable name")
except:
	print("There's something wrong with your code")
```

```
# COMMENTS
# this is a comment
"""
this is
a multi-line comment 
yay
"""
```
