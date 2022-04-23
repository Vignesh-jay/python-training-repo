#simple function
def prin():
    print("\nhello world \n")
    print("good day\n")

prin()

#Calling funtion with returns

def fun():
    a=int(input("Enter a Value : "))
    b=int(input("enter b Value : "))
    c=a*b
    return c

print("the a * b value is ",fun())
