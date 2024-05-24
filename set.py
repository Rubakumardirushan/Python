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