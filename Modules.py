
#random module

# Dice rolling Program

from random import randrange
x=0
for num in range(0,2):
    value=randrange(1,6)
    if value==1:
        print("One : *")
    elif value==2:
        print("Two : **")
    elif value==3:
        print("Three : ***")
    elif value==4:
        print("Four : ****")
    elif value==5:
        print("Five : *****")
    elif value==6:
        print("Six : ******")
    else:
        print("Error...!")
    x += value
print("your value is : ",x)
