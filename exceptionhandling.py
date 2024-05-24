import sys
num=[1,'a',0,1]
for i in num:
    try:
        print("The entry is",i)
        r=1/int(i)
        break
    except:
        print("Oops!",sys.exc_info()[0],"occured.")
        print("Next entry.")
        print()