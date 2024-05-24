f=open("if.py")
print(f.read())
## write file write code


## not delete old content only add new content
f=open("dirushan.txt","a")
f.write("hello")
f=open("dirushan.txt")
print(f.read())