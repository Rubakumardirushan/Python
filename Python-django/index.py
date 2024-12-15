print("hello world")
"""
 ##1. Variables and Data Types
 #python
#Copy code 
# Variables and Data Types
name = "Dirushan"         # String
age = 22                   # Integer
height = 5.9               # Float
is_student = True          # Boolean

print(name, age, height, is_student)


##input output 

age= input("Enter your age: ")
print("Your age is: ", age)
name = input("Enter your name: ")
print("Your name is: ", name)


age_string="26"
age_int=int(age_string)
print(age_int)
print(type(age_int))
print(type(age_string))



### if else 
number=int(input("Enter a number: "))
if number%2==0:
    print(f"{number} is even")
    if(number%4==0):
            print(f"{number} is divisible by 4")
    else:
        print(f"{number} is not divisible by 4")
else:
    print(f"{number} is odd")


"""
##2. Loops
# for loop
for i in range(1, 5):
     for j in range(1, 5):
         print(j,end=" ")
     print('')   