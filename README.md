# Python-Udemy-Tutorial

### All the basics

Multiple Assignment
instead of : diana = 20, alex = 17, dana = 21, we can write:
```
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
# Dictionaries
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
# Tuples
# are immutable : you cannot change them, delete from/update. Only access
# you can combine 2 tuples together: tup3 = tup1 + tup2
# del tup, len tup, tup + 4
tup = ('tulips','roses')
```
