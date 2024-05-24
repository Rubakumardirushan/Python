# set not conatin duplicate value
# set is unordered
# set is mutable

# set is created by using {}
# set is created by using set() function
# set is created by using set comprehension
number=['one','two','three','four','five','one','two','three','four','five'] #list
num_set=set(number) #set
print(num_set)
num_set.add('six')
print(num_set)



my_list=[1,4,2,3,8,5,6,7,9,10,1,4,2,3,8,5,6,7,9,10]
my_set=set(my_list)
print(my_set)
my_set.add(11)
print(my_set)


a={1,2,3,4,5,6,7,8,9,10}
b={5,6,7,8,9,10,11,12,13,14}
print(a^b)
print(a|b)
print(a&b)



# dictinory
# key value pair
# key must be unique
# key must be immutable
# key must be string or number
# key must be tuple
# key must be set
# key must be frozenset

# value can be any data type
dict1={'name':'dirushan','age':25,'city':'colombo'}
print(dict1['age'])
dict1['age']=262
print(dict1['age'])
del dict1['age']
print(dict1)
dict1['age']=25
print(dict1)


#range
# range is a class
# range is immutable
# range is created by using range() function
# range is created by using range comprehension
# range is created by using :
# range is created by using step
# range is created by using negative value
# range is created by using negative step
# range is created by using negative value and negative step
# range is created by using negative value and positive step
# range is created by using positive value and negative step
print(range(1,10))
number=range(1,10)
list1=list(number)
tuple1=tuple(number)
set1=set(number)
print(list1)
print(tuple1)
print(set1)


num="sccw"
if num in number:
    print("yes")
else:
    print("no")